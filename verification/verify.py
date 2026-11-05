#!/usr/bin/env python3
"""红嫁衣 / MONST(H)ER 自动检查。

用法（在项目根目录）:
    python3 verification/verify.py                 # 默认检查 monst(h)er.html 对照 最新版本文案/ 下的英文 docx
    python3 verification/verify.py --html X.html --script Y.docx

检查项:
  1. JS 能否解析（用 macOS osascript 的 JavaScriptCore，或 node）
  2. 红嫁衣线的剧情文字是否逐字出现在最新英文剧本中（经用户确认的例外见 APPROVED_TEXT）
  3. 理论框文字是否出现在最新剧本中
  4. 对话框名牌是否来自剧本（"Name:"）或经用户确认
  5. 图片序列（film / outs）结构是否完整
  6. 页面引用的图片文件是否存在、体积是否过大
  7. 已确认的交互约定（立绘不翻转等）
  8. 覆盖度：剧本里每一句剧情是否都出现在游戏中（默认 WARN，--strict 时为 FAIL）

FAIL 项会让脚本以退出码 1 结束；WARN 只提示。
"""
import argparse
import glob
import html as htmllib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 经用户确认、允许不逐字出现在剧本里的剧情文字（来源见 memory/decisions.md）
APPROVED_TEXT = {
    "You step softly toward the door.": "D-T3 用户指定把旁白截到这里（2026-11-03）",
}
# 经用户确认的名牌（剧本里没有对应的 "Name:"）
APPROVED_NAMES = {
    "A Man": "D-T4 运粮男人的名牌（2026-11-03）",
}
UI_KEYS = {"img", "bg", "cls", "place", "time", "stage", "label", "scale", "who"}
BIG_FILE = 3 * 1024 * 1024


# ---------- 读取 ----------
def docx_paras(path):
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    paras = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S):
        p = re.sub(r"<w:tab/>|<w:br[^>]*/>|<w:cr/>", "<w:t> </w:t>", p)  # 段内换行也是句子分隔
        paras.append(norm(htmllib.unescape("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, flags=re.S)))))
    return [x for x in paras if x]


def norm(s):
    return re.sub(r"\s+", " ", s.replace(" ", " ")).strip()


def find_script(arg):
    if arg:
        return arg
    cands = [f for f in glob.glob(os.path.join(ROOT, "最新版本文案", "*.docx"))
             if not os.path.basename(f).startswith((".~", "~$")) and re.search(r"EN", os.path.basename(f))]
    if len(cands) != 1:
        sys.exit(f"找不到唯一的英文剧本（最新版本文案/*EN*.docx）：{cands}，请用 --script 指定")
    return cands[0]


def load_data(html_src):
    """用真实 JS 引擎执行页面脚本（不渲染），取出 data.red；同时完成语法检查。"""
    m = re.search(r"<script>(.*)</script>", html_src, flags=re.S)
    if not m:
        return None, "找不到 <script>"
    code = m.group(1)
    code = re.sub(r"render\(\);\s*$", "", code.rstrip())  # 不执行首屏渲染
    stub = "var document={getElementById:function(){return {}}};var window={scrollTo:function(){}};\n"
    engines = []
    if shutil.which("osascript"):
        engines.append(("osascript", ["osascript", "-l", "JavaScript"], "\nJSON.stringify(data.red)"))
    if shutil.which("node"):
        engines.append(("node", ["node"], "\nconsole.log(JSON.stringify(data.red))"))
    if not engines:
        return None, "没有可用的 JS 引擎（需要 macOS osascript 或 node）"
    name, cmd, tail = engines[0]
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(stub + code + tail)
        tmp = f.name
    try:
        r = subprocess.run(cmd + [tmp], capture_output=True, text=True, timeout=60)
    finally:
        os.unlink(tmp)
    if r.returncode != 0:
        return None, f"{name} 执行失败（多半是 JS 语法错误）：{r.stderr.strip()[:400]}"
    return json.loads(r.stdout), None


SECTION = re.compile(r"^(Opening(?=:)|Prologue|Scene \d+|Ending [A-Z]|Final Screen)\b")
SKIP_PARA = re.compile(r"^(Theoretical Connection|Phoenix \(|Player Choices|Only players|BGM:|Opening Cultural Note)")
SPEAKER = re.compile(r"^(?:[A-Z][a-z]+(?: [A-Z][a-z]*)?|You): ")


def script_sentences(paras):
    """剧本中玩家应当看到的句子，按章节分组（只取 Opening/Prologue 到 THE END 之间）。"""
    out, sec = {}, None
    for p in paras:
        if p.startswith("THE END"):
            break
        m = SECTION.match(p)
        if m:
            sec = m.group(1)
            if p.startswith("Opening:"):
                p = p.split(":", 1)[1].strip()
            else:
                continue
        if not sec or SKIP_PARA.match(p):
            continue
        p = re.sub(r"\s*→ Proceed to [^.]*\.?|\s*→ Ending [A-Z]\.?", "", p)
        p = re.sub(r"^[A-Z]\. ", "", p)                  # 选项前的 "A. "
        for piece in re.split(r"(?<=[.!?…”])\s+|\s+(?=\()|(?<=\))\s+", p):  # 舞台提示 (…) 也单独成句
            piece = SPEAKER.sub("", piece.strip())
            if len(piece) > 1:
                out.setdefault(sec, []).append(piece)
    return out


# ---------- 遍历 ----------
def walk(node, keys=()):
    """产出 (键路径, 字符串)。数组里的元素沿用数组的键。"""
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk(v, keys + (k,))
    elif isinstance(node, list):
        for v in node:
            yield from walk(v, keys)
    elif isinstance(node, str):
        yield keys, node


def films(red):
    for i, s in enumerate(red.get("scenes", [])):
        if s.get("film"):
            yield f"scenes[{i}].film（{s.get('title')}）", s["film"]
        for j, o in enumerate(s.get("outs") or []):
            if o:
                yield f"scenes[{i}].outs[{j}]（{s.get('title')} · 选项{'AB'[j] if j < 2 else j}）", o


# ---------- 检查 ----------
class Report:
    def __init__(self):
        self.rows = []

    def add(self, level, section, msg):
        self.rows.append((level, section, msg))

    def show(self):
        icon = {"PASS": "✔", "WARN": "!", "FAIL": "✖"}
        cur = None
        for level, section, msg in self.rows:
            if section != cur:
                print(f"\n== {section} ==")
                cur = section
            print(f"  {icon[level]} {msg}")
        fails = sum(r[0] == "FAIL" for r in self.rows)
        warns = sum(r[0] == "WARN" for r in self.rows)
        print(f"\n结果：{fails} 个 FAIL，{warns} 个 WARN")
        return fails


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", default=os.path.join(ROOT, "monst(h)er.html"))
    ap.add_argument("--script")
    ap.add_argument("--all", action="store_true", help="列出全部不一致文字（默认每类最多 40 条）")
    ap.add_argument("--strict", action="store_true", help="最终交付：覆盖度不足也算 FAIL")
    a = ap.parse_args()
    rep = Report()
    limit = None if a.all else 40

    script = find_script(a.script)
    paras = docx_paras(script)
    doc = norm(" ".join(paras))
    html_src = open(a.html, encoding="utf-8").read()
    print(f"页面：{os.path.relpath(a.html, ROOT)}\n剧本：{os.path.relpath(script, ROOT)}（{len(doc)} 字符）")

    # 1. JS
    red, err = load_data(html_src)
    if err:
        rep.add("FAIL", "1 JS 解析", err)
        return rep.show()
    rep.add("PASS", "1 JS 解析", "页面脚本可以解析并执行到数据定义")

    # 2–4. 文字
    story, theory, names, other = [], [], set(), []
    for keys, s in walk(red):
        top = keys[0] if keys else None
        if top not in ("scenes", "endings", "final"):
            if top in ("ending", "archive", "intro", "label"):
                other.append((keys, s))
            continue
        if keys[-1] == "who":
            names.add(s)
        if keys[-1] in UI_KEYS or (keys[-1] == "then" and s in ("choice", "next")):
            continue
        (theory if "basis" in keys else story).append((keys, s))

    def check(items, section):
        seen, bad = set(), []
        for keys, s in items:
            t = norm(s)
            if not t or t in seen:
                continue
            seen.add(t)
            if t in doc or t in APPROVED_TEXT:
                continue
            bad.append((".".join(k for k in keys if not k.isdigit()), t))
        if bad:
            rep.add("FAIL", section, f"{len(bad)}/{len(seen)} 段文字不在最新剧本中：")
            for path, t in bad[:limit]:
                rep.add("FAIL", section, f"[{path}] {t[:110]}{'…' if len(t) > 110 else ''}")
            if limit and len(bad) > limit:
                rep.add("FAIL", section, f"……另有 {len(bad) - limit} 条，用 --all 查看")
        else:
            rep.add("PASS", section, f"{len(seen)} 段文字全部逐字出现在剧本中")

    check(story, "2 剧情文字 ⇄ 最新剧本")
    check(theory, "3 理论框文字 ⇄ 最新剧本")
    for n in sorted(names):
        if f"{n}:" in doc:
            rep.add("PASS", "4 名牌", f"{n}（剧本中有 “{n}:”）")
        elif n in APPROVED_NAMES:
            rep.add("PASS", "4 名牌", f"{n}（{APPROVED_NAMES[n]}）")
        elif re.search(r"(?<![\w’'])" + re.escape(n) + r"(?![\w’'-])", doc):
            rep.add("PASS", "4 名牌", f"{n}（剧本正文中原样出现）")
        else:
            rep.add("FAIL", "4 名牌", f"{n}：剧本中没有，也未经确认")
    stale = sum(norm(s) not in doc for _, s in other)
    if stale:
        rep.add("WARN", "4b 其他可见文字", f"结局页/档案页等旧文字中有 {stale} 段不在最新剧本中（尚未按剧本重做的页面）")

    # 5. 图片序列结构
    refs = set()
    any_film = False
    for where, fm in films(red):
        any_film = True
        beats = fm.get("beats") or []
        ends = [i for i, b in enumerate(beats) if "end" in b]
        if len(ends) != 1 or ends[0] != len(beats) - 1:
            rep.add("FAIL", "5 图片序列结构", f"{where}：必须且只能在最后有一个 end 步骤")
        if not beats or "bg" not in beats[0]:
            rep.add("WARN", "5 图片序列结构", f"{where}：第一步不是 bg（底图）")
        for b in beats:
            if "bg" in b:
                refs.add(b["bg"])
            for t in b.get("talk", []):
                miss = [k for k in ("who", "img", "text") if not t.get(k)]
                if miss:
                    rep.add("FAIL", "5 图片序列结构", f"{where}：对话缺少 {miss}")
                if t.get("flip"):
                    rep.add("FAIL", "7 已确认约定", f"{where}：{t.get('who')} 设置了 flip（立绘不翻转，见 C-01）")
                refs.add(t.get("img", ""))
        if beats and beats[-1].get("then") not in ("choice", "next"):
            rep.add("FAIL", "5 图片序列结构", f"{where}：end 的 then 必须是 choice 或 next")
    if any_film and not any(r[1].startswith("5") for r in rep.rows):
        rep.add("PASS", "5 图片序列结构", "所有图片序列结构完整")

    # 6. 资源文件
    for m in re.finditer(r"""(?:src|href)=["']([^"'$]+)["']|url\(["']?([^"')$]+)["']?\)""", html_src):
        p = m.group(1) or m.group(2)
        if p and not p.startswith(("data:", "http", "#", "mailto:")):
            refs.add(p)
    refs.discard("")
    base = os.path.dirname(os.path.abspath(a.html))
    missing = [r for r in sorted(refs) if not os.path.exists(os.path.join(base, r))]
    for r in missing:
        rep.add("FAIL", "6 资源文件", f"找不到：{r}")
    big = [(r, os.path.getsize(os.path.join(base, r))) for r in sorted(refs) if r not in missing and os.path.getsize(os.path.join(base, r)) > BIG_FILE]
    for r, n in big:
        rep.add("WARN", "6 资源文件", f"{r} 有 {n / 1048576:.1f}MB，正式交付前建议压缩")
    if not missing:
        rep.add("PASS", "6 资源文件", f"{len(refs)} 个引用的文件都存在")

    # 7. 已确认约定（CSS/代码层面的守卫）
    guards = [
        (".rb-card.filming{height:", "图片序列播放时卡片高度固定（C-04）"),
        (".rb-film.closing .rb-film-skip{display:none}", "收尾旁白期间隐藏 Skip（C-05）"),
        ("const tail=", "Skip 只跳过对话、落在收尾旁白（C-05）"),
        ("const rbChunks=", "底图上的旁白按句子分组显示（D-F10）"),
        ("const RB_SAVE=", "刷新后停留在原页面（D-L5）"),
    ]
    for needle, what in guards:
        rep.add("PASS" if needle in html_src else "FAIL", "7 已确认约定", what)

    # 8. 覆盖度（剧本 → 游戏）
    corpus = norm(" ".join(s for _, s in story))
    level = "FAIL" if a.strict else "WARN"
    for sec, sents in script_sentences(paras).items():
        miss = [x for x in sents if x not in corpus]
        if not miss:
            rep.add("PASS", "8 覆盖度（剧本 → 游戏）", f"{sec}：{len(sents)} 句全部在游戏中")
            continue
        rep.add(level, "8 覆盖度（剧本 → 游戏）", f"{sec}：{len(miss)}/{len(sents)} 句不在游戏中，例如：{miss[0][:90]}")
        if a.all:
            for x in miss[1:]:
                rep.add(level, "8 覆盖度（剧本 → 游戏）", f"    {x[:110]}")

    return rep.show()


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
