# 进度（progress）

最后更新：2026-11-04

## 当前状态一览
| 部分 | 排版 / 画面 | 文字版本 |
|---|---|---|
| Opening（V3 新增：红嫁衣拜灵位的开场画面 + 文化说明 + BGM） | 未做 | — |
| Prologue | ✅ 图片序列（井边 → 选 A / 选 B：门边偷听 → 父亲推门） | ✅ 与 V3 一致 |
| Scene 1 | ✅ 图片序列（粮车；A：父女对话；B：母女床边） | ✅ 与 V3 一致（2026-11-04 同步） |
| Scene 2 | ✅ 开场、A、B 都已做成图片序列（村口；A：07A → 07B；B：08B → 09B → 10B（司机）→ 11B → 12 窗边） | ✅ 与 V3 一致 |
| Scene 3 | ✅ 开场、A、B 都已做成图片序列（A：13A → 16A → 11B；B：13B v2 → 14B v2（村长）→ 11B） | ✅ 与 V3 一致（含 2026-11-05 剧本改动 “kneel at him”） |
| Scene 4 | ✅ 开场是图片序列（17 进门 → 18 母女并坐对话 → 19 女主视角，出现选项）；A 结果也是图片序列（19 上女主台词与旁白 → 20A 铜镜梳头 + 共用收尾段 + Continue）；B 结果也是图片序列（20B 争吵 → 21B 被锁 → 22 清晨梳妆） | ✅ 与 V3 一致（2026-11-04 同步） |
| Scene 5 | ✅ 开场是图片序列（23 → 24 → 25 → 26 → 19 → 27，最后出现选项）；A 结果（28 轿内 → 29 陈家门前）和 B 结果（27 上显示第一句 → 31B 揭盖头凝视金钗 → 32B 金钗落在嫁衣上 → 30 陈家门口）也都是图片序列 | ✅ 与 V3（2026-11-05 19:28 版）一致 |
| Scene 6 | ✅ 开场（33 → 34 → 35 → 41 → 35 → 38 → 40 → 42 → 喂药，出现选项）、A 结果（红盖头 → 放进棺材 → 47B → 棺内 → 合上棺材 → 变黑）、B 结果（49B → 50B → 51B）都是图片序列 | ✅ 与 V3（2026-11-06 10:45 版）一致 |
| Ending A/B/C | ✅ 图片序列（A：30 → 放进棺材 → 53；B：52；C：49B → 红盖头 → 放进棺材 → 47B → 棺内 → 合上棺材 → 变黑） | ✅ 与 V3 一致 |
| Final Screen | ✅ 图片序列（55 → 54 → 56，THE END） | ✅ 正文与 V3 一致（理论框仍是 V2） |
| 理论框（Scene 1–4、6、Final） | 可折叠框 | ⚠️ V2（Berlant & Warner），V3 改成了 Phoenix (2006) |
| 档案页 / 选角页 / 介绍页 | 旧版，没有重做 | ⚠️ 介绍页和档案页讲的仍是 Berlant & Warner |

`verify.py` 基线：2026-11-04 初次运行为 **36 FAIL / 8 WARN**；同步剧情文字后为 **19 FAIL / 3 WARN**。剧情文字 185 段全部逐字对上 V3，覆盖度只差 Opening。剩下的 FAIL 全部是理论框（Q3），WARN 是 Opening、旧档案页文字和一张 3.2MB 的底图。

## 已完成（按时间）
1. 2026-11-03 红嫁衣剧情页改为“信息栏 + 卡片 + 虚线选项”布局；文字改为逐步显现；选择结果另起一页。
2. 2026-11-03 Prologue 到 Scene 6、三个结局、Final Screen 的文字按 V2 剧本替换完毕。
3. 2026-11-03 写好通用的图片序列播放器（底图、旁白、对话、结尾），Prologue 和 Scene 1（包括 A/B 两个选项）都改成了图片序列。
4. 2026-11-03 修复：卡片高度固定（C-04）、Skip 不再跳过收尾旁白（C-05）、序列结束后的点击无效。
5. 2026-11-04 建立协作系统：CLAUDE.md、corrections、decisions、progress、checklist、verify.py。
6. 2026-11-04 小范围文字同步到 V3（13 处）：Scene 1（A/B 对话、舞台提示、共用收尾段新增两句）、Scene 2（正文最后一段、A 中父亲的台词）、Scene 3（共用收尾段）、Scene 4（母亲两句台词、正文新增一句）、Final Screen 正文。没有改动布局和交互。备份文件为 scratchpad/monst(h)er.before-v3-text.html。
7. 2026-11-04 Scene 2 开场改为图片序列：底图 06_村口流言；旁白 → 7 句对话（Old Woman / Neighbor / Villager A / Villager B，scale 0.75）→ 旁白 “You stop in your tracks…” → 结尾句 “Why does everyone…” 加两个选项。新增半身图：角色立绘/老妇人、邻人、村民甲、村民乙_半身.png。用自然速度完整走过一遍（约 85 秒），verify 剧情文字 185/185 通过。
8. 2026-11-04 底图上的旁白按句子分组显示（D-F10），所有图片序列都适用。拆分后重新拼起来与原文完全一致。目前最长的一组是单独一句 151 字（Scene 1 收尾的 “For the first time, you realize…”，没有可以断开的标点）。备份文件为 scratchpad/monst(h)er.before-chunks.html。
9. 2026-11-05 Scene 2 A 改为图片序列：07A 上进行 5 句父女对话（“You rush home.” 放在第一句的舞台提示行）→ 交叉淡化到 07B → 生气父亲的台词（舞台提示行为 “Your father slams his hand on the table.”）→ 旁白 “Your mother stands by the door without a word.” → 共用收尾段拆组显示，加 Continue。新的中间标签是 “Scene 2 · The Li Family Kitchen”。用自然速度完整走过一遍（约 80 秒），剧情文字 189/189 通过。开工前重新提取了 V3 剧本，文字没有变化。
10. 2026-11-05 Place 随底图更新（D-F11：Scene 1 B 显示 Inside the House，Scene 2 A 显示 The Li Family Kitchen）；换底图时隐藏中间标签（D-F12）。已在浏览器里确认 Scene 2 A、Scene 1 B、Prologue B 的效果。备份文件为 scratchpad/monst(h)er.before-place.html。
11. 2026-11-05 Time 也随画面变化：任何步骤都可以带 `time`。Scene 2 A 收尾 “You lie awake all night…” 显示 That Night。已在浏览器里确认切换时机，Skip 跳到结尾时显示也正确。备份文件为 scratchpad/monst(h)er.before-time.html。
12. 2026-11-05 Scene 2 B 改为图片序列，共 5 张底图：08B 逃离村口 → 09B 岔路背影 → 10B 黄昏马车（Driver 对话；“You lower your head.” 作为旁白）→ 11B 夜晚返村 → 12 窗边未眠（共用收尾段加 Continue）。新增半身图：角色立绘/车夫_半身.png。Place/Time 依次为 The Village Edge / The Next Day → A Fork in the Road → A Fork in the Road / Dusk → The Village / Nightfall → Your Bedroom / That Night（待用户确认）。用自然速度完整走过一遍（约 80 秒），剧情文字 194/194 通过。
13. 2026-11-05 Scene 3 开场改为图片序列：底图沿用午后井边洗衣（place 为 The Li Courtyard），正文拆成两组，第二组 “But you refuse to simply accept your fate. You decide to seek help.” 留在画面上并显示选项。用自然速度走过一遍；选择之后仍进入卡片结果页（Place 回到这一幕原来的 The Village）。
14. 2026-11-05 刷新后停在原处（D-L5，sessionStorage）。已测试：图片序列中的对话（Scene 2 B 的 Driver，Scene 1 A 的第 5 句）、结尾画面加选项、卡片结果页、Mohini 页，刷新后都恢复到原处。备份文件为 scratchpad/monst(h)er.before-resume.html。
15. 2026-11-05 Scene 3 A 改为图片序列：13A 旁白 → A-Yue（舞台提示 “A-Yue takes your hands.”）→ 14A A-Yue（“She takes out a jade pendant.”）→ 15A A-Yue’s father（“The door is suddenly pushed open…”）→ 16A A-Yue（“A-Yue looks at you, her eyes red.”）→ 共用收尾段拆组显示，加 Continue。新增半身图：角色立绘/阿月_半身.png、阿月父亲_半身.png。因为 15A/16A 里的女主在左前景，本段立绘统一缩到 0.65（C-02）。Place 为 A-Yue’s Home。verify 的名牌检查放宽为“剧本正文中原样出现的名字也通过”（A-Yue、A-Yue’s father）。用自然速度走过一遍（约 100 秒），剧情文字 202/202 通过。
16. 2026-11-05 Scene 3 A 收尾改用 11B 夜晚返村底图。同时修复一处 D-F12 的漏洞：对话结束、下一步要换底图时，中间标签会在旧底图上闪现约 0.8 秒；现在会一直隐藏到换图后的旁白出现。所有“对话 → 换底图”的地方都已修复。备份文件为 scratchpad/monst(h)er.before-s3a-walkhome.html。
17. 2026-11-05 Scene 3 B 改为图片序列：13B v2 上先旁白，再接女主的台词 → 14B v2 上 5 句对话（Village Head 第一句的舞台提示为 “The village head sets down his teacup.”，最后一句为 “…avoids your eyes.”）→ 11B 收尾加 Continue。新增半身图：角色立绘/村长_半身.png。Place 为 The Village Head’s Home，回村部分为 The Village。
    - 剧本 V3 又更新了一处：“kneel at his door” 改成 “kneel at him”，游戏里已同步（C-08：一开始没发现剧本已更新）。
    - 修复一个 bug：如果在结尾画面出现后 2.6 秒内离开，结尾画面设下的定时器会把下一页的理论框提前显示出来；现在定时器会先确认画面还在。
    - 用自然速度走过一遍（约 110 秒），剧情文字 206/206 通过。
18. 2026-11-05 用户把 `角色立绘/` 移到了 `红嫁衣角色立绘/角色立绘/`；按用户决定把 html 里的 23 处立绘路径改到新位置，33 个图片引用全部能加载。建立 git 仓库（main 分支，本项目内的作者为 maomonica），首次提交 fb75763：76 个文件，约 83MB，排除了 zip 备份、Word 锁文件、.DS_Store 和 __pycache__。2026-11-05 已推送到私有仓库 https://github.com/Monica11110702/NMC5369-Gender-media-project （origin/main = 6983771，76 个文件）。推送方式：在终端用 HTTPS，加上有 repo 权限的 Classic Personal Access Token，凭据已存入 macOS 钥匙串。以后上传时：Claude 负责提交，再运行 `git push`（或者用户在终端里推送）。
19. 2026-11-05 用户把游戏文件 `monst(h)er.html` 改名为 `index.html`（内容和 6983771 提交的版本完全相同）。此后在 index.html 上修改；verify 要加 `--html index.html` 运行，预览地址是 http://localhost:8765/index.html。CLAUDE.md、verify.py 默认路径、checklist 等处仍写着旧文件名，要不要改等用户决定。
20. 2026-11-05 Scene 4 开场改为图片序列：17 女主进门（开场旁白分组）→ 18 母女并坐（Mother/You 共 11 句对话；“Your mother falls silent.” 和 “Your mother lowers her head and straightens the dress.” 放进母亲台词的舞台提示行）→ 19 女主视角看母亲（从 “You look at your mother” 开始的收尾段分组，最后一组和选项一起出现）。立绘用 母亲_半身 / 主角_半身，scale 为 1：截图确认没有挡住 18 里两个人的脸（女主立绘的右边缘贴近底图女孩的手臂）。Place/Time 沿用 Your Bedroom / The Day Before the Wedding。剧本重新提取后只有空白字符不同（C-08）。用自然速度走完一遍（约 100 秒），底图高度 680px，与序章一致；结尾画面刷新后能恢复；选 A 后进入原来的卡片结果页。verify：剧情文字 210/210 通过，19 FAIL（理论框，未变）/ 6 WARN（未变）。备份文件为 scratchpad/index.before-scene4-film.html。
21. 2026-11-05 Scene 4 A 结果改为图片序列：沿用 19 女主视角底图 → You 对话（舞台提示 “You lower your head.”）→ 旁白 “Your mother lets out a relieved breath.” → 换 20A 铜镜前母亲梳头 → “You sit before the bronze mirror…” 分组 → 共用收尾段 “Early the next morning…” 分组，最后一组加 Continue，理论框随 Continue 出现。主角立绘 scale 1：在 19 上挡住了母亲的发髻和肩膀，但没挡脸（C-02 已截图确认）。Time 没有改成第二天早上（D-F11 待用户确认）。用自然速度走了一遍（约 60 秒）；中途刷新能从 20A 那一句继续；选 B 仍进入卡片结果页。verify：剧情文字 213/213 通过，19 FAIL / 6 WARN（都是改之前就有的）。备份文件为 scratchpad/index.before-scene4-A.html。
22. 2026-11-05 Scene 4 B 结果改为图片序列：20B 婚前与父母争吵（Place 为 The Li Family Kitchen）上三句对话：You（舞台提示 “You stand before your parents.”）→ Father 用生气立绘（舞台提示 “Your mother begins to cry in fright. Your father’s face darkens.”，两句在剧本中相邻）→ You → 换 21B 被锁屋内（Place 为 The Li Courtyard）：旁白 “Your father calls in family members…” → Father “She is not to leave…” → 旁白 “You pound on the door…” → 换 22 婚礼清晨梳妆（Place 为 Your Bedroom）显示共用收尾段，加 Continue。Place 只用已经确认过的地点名称。20B 里女主在左侧，立绘挡住了她的下半身，所以本段立绘统一缩到 0.65（C-02），已截图确认没有挡住脸。用自然速度走了一遍（约 85 秒），刷新后能从中途恢复。verify：剧情文字 219/219 通过，19 FAIL / 7 WARN（新增的 WARN 是 21B 有 3.0MB）。备份文件为 scratchpad/index.before-scene4-B.html。
23. 2026-11-05 剧本 V3 docx 又更新了（19:28），重新提取后 diff 发现 Scene 5 有两处改动：开场的 “Through the curtain, you see villagers lining the roadside.” 改成 “Villagers lining the roadside.”；A 结果的 “You take a deep breath and lower the curtain.” 改成 “You take a deep breath.”。第一处属于这次任务范围（用户引用的就是新写法），已同步到 body；第二处等用户决定（verify 会因此报 1 个 FAIL）。
24. 2026-11-05 Scene 5 开场改为图片序列，每张底图配一句或一段：23 花轿离村 → 24 唢呐队 → 25 路旁村民（分两组）→ 26 父亲（女主视角）配父亲那句话 → 19（复用）配母亲那句话 → 27 轿内低头看嫁衣，从 “You look down at your red bridal dress.” 开始分组，最后一组和选项一起出现。没有对话框，也没有新的 Place；Place 和 Time 沿用 The Bridal Sedan Chair / The Wedding Day。25 的尺寸是 1752×897，比其他底图更宽，左右裁切也更多：最右边的女孩在卡片里只露出一部分。用自然速度走了一遍（约 78 秒），底图高度 680；中途刷新能停在 26 那一句。verify：21 FAIL（19 个理论框 + 剧本更新导致的 1 个 A 结果，另 1 个是理论框数量的计数），8 WARN。备份文件为 scratchpad/index.before-scene5-film.html。
25. 2026-11-05 Scene 5 A 结果改为图片序列：28 女主坐在花轿内，You 的对话框（舞台提示 “You take a deep breath.”，台词 “As long as I am alive…”，立绘 scale 1，没挡住新娘）→ 29 花轿停在陈家门前，显示 “The bridal sedan chair continues forward…”，加 Continue。用户引用的是新剧本的写法，所以同步把 opts 里的 “You take a deep breath and lower the curtain.” 改为 “You take a deep breath.”（第 23 条里待定的那处）。用自然速度走了一遍（约 20 秒）；点 Continue 进入 Scene 6，日志里记录的是新文字。注意：主角半身立绘穿的是蓝布衣，而 28 里的新娘穿红嫁衣、盖着盖头，两者服装不一致。verify：剧情文字 226/226 通过，19 FAIL（理论框）/ 7 WARN。备份文件为 scratchpad/index.before-scene5-A.html。
26. 2026-11-05 用户同意处理连带改动：
    - 文件名：CLAUDE.md（3 处）和 verify.py（默认路径和注释）改为 index.html；现在直接运行 `python3 verification/verify.py` 就会检查 index.html。
    - Q17：图片序列中间的标签跟着 Place 变（改 `rbSetPlace`，刷新恢复也改用它）。在浏览器里逐个检查了 17 段序列的结尾画面，标签都和 Place 一致；Scene 4 B 用自然速度走了一遍，标签依次为 Kitchen → Courtyard → Your Bedroom；中途刷新能恢复正确的标签。verify 新增守卫字符串。
    - Q16：Scene 4 A/B 的收尾 “Early the next morning…” 出现时，Time 改为 The Wedding Day。
    - 没做的：Scene 5 B 的图片序列，以及 Q18 嫁衣立绘，这两项都需要用户提供素材。
    - 测试中再次碰到 Q8：预览窗口被隐藏时动画会卡住，重新显示后恢复，这不是这次改动导致的。
    - 备份：scratchpad/index.before-label-time.html、CLAUDE.before-rename.md、verify.before-rename.py。
27. 2026-11-06 Scene 5 B 结果改为图片序列，全部是旁白：31B 揭开盖头凝视金钗 → 32B 金钗落在嫁衣上 → 30 陈家门口近景（收尾，按钮是原有的 “Reveal the ending”，点击后进入 Ending A）。用户是从 “Unwilling to let others…” 开始指定 31B 的；B 段的第一句 “You know the bridal sedan chair is drawing closer to the Chen household.” 一开始放在了 31B 上；用户随后决定把它留在选择前的底图 27 轿内上（2026-11-06 已改，并用自然速度验证：0.4–5 秒显示在 27 上，之后换到 31B；备份文件为 scratchpad/index.before-scene5-B-first.html）。Place 沿用 The Bridal Sedan Chair（30 实际是陈家门口，没有起新地点名）。用自然速度走了一遍（约 32 秒）；endingVariant 为 A，进入 “The Last Refusal”（Ending A）。verify：剧情文字 228/228 通过，19 FAIL（理论框）/ 7 WARN。备份文件为 scratchpad/index.before-scene5-B.html。
28. 2026-11-06 整体开头和结尾按新版 html 替换（D-L6）：新开头、角色选择页、What If 页、共用页都已加入；旧的 Berlant 介绍页和旧选角页已删除。档案页（仍是 Berlant 框架）保留在流程里（“别的不变”），What If 接在档案页之后。两张封面图从 CSS 移到 JS 常量 `MH_IMG`，和新 html 里的图完全相同，没有增加文件体积。已测试：开头 → 按钮 → 角色页 → 红嫁衣序章（故事页样式不变，底图高度 680）；Mohini 进入原有故事；档案 → What If（两个故事的选项不同）→ 共用页 → 按钮跳转；What If 刷新后恢复选择；手机宽度下开头大标题原本会撑出横向滚动（新版 html 也有这个问题），已在 760px 以下把标题改为 12vw，复测后四个页面都没有横向滚动；控制台无报错。没有完整重玩整条故事线（故事页的代码和数据没有改动）。verify：剧情文字 230/230 通过，19 FAIL（理论框）/ 7 WARN；新增 3 项检查。备份文件为 scratchpad/index.before-new-opening.html。
29. 2026-11-06 按用户决定：首页去掉 Return home（角色页、What If、共用页保留）；档案页整页删除（渲染分支和 `uncover` 都已移除），红嫁衣 Final Screen 和 Mohini 结局页原来的 “Recover her story →” 改为 “Ask: What if? →”。如果刷新时保存的页面还是旧的 archive，会自动进入 What If。已测试：红嫁衣结局 B → Final Screen（自然速度）→ What If；Mohini 结局 → What If；旧存档跳转；控制台无报错。data 里的 `archive` 字段和 `theory.counter` 没有再被使用，暂时保留。Mohini 结局页的 “How the legend remembers her / What is missing from this description?” 面板未改。verify：剧情文字 230/230 通过，19 FAIL / 7 WARN。备份文件为 scratchpad/index.before-remove-archive.html。
30. 2026-11-06 剧本又更新（10:45）：Scene 6 的 “Madam Chen studies you carefully.” 改成 “Madam Chen looks at you carefully.”。用户消息里写的是 looked，这里按剧本用 looks，并已同步到 body。
31. 2026-11-06 Scene 6 开场改为图片序列：33（下轿旁白）→ 34（灵位旁白、Old Woman、“You take the teacup…”）→ 35（“You kneel and offer the tea.”）→ 41（Madam Chen，舞台提示 “Madam Chen looks at you carefully.”；Master Chen）→ 35（You / Madam Chen / You / Old Woman，舞台提示 “The ancestral hall suddenly falls silent. The old woman steps behind you.”）。用户只指定到 “…forever.”；后面的段落（侧门、质问、收尾）为了不丢文字，暂时都放在 35 上，选项也出现在 35，等用户指定。新增半身图：陈老爷_半身、陈夫人_半身、女主_嫁衣定稿_半身（放在 `红嫁衣角色立绘/`，按 D-A1 裁剪）。本幕 You 都用嫁衣立绘；Old Woman 沿用 老妇人_半身（头巾、拄拐，和底图里的老妇人不是同一个样子）；立绘 scale 全部 0.65，截图确认没有挡脸。用自然速度走了一遍（约 195 秒），底图高度 680；选 A 进入卡片结果页。verify：剧情文字 237/237 通过，19 FAIL（理论框）/ 7 WARN。备份文件为 scratchpad/index.before-scene6-film.html。
32. 2026-11-06 换立绘：用户新放入 `祠堂老妇人_全身透明立绘.png`，按 D-A1 裁成 `祠堂老妇人_半身.png`，Scene 6 的两处 Old Woman 换成它（Scene 2 的村里老妇人不变）。Scene 5 A 的 You 换成 `女主_嫁衣定稿_半身.png`；嫁衣立绘比蓝布衣宽，会压到 28 里新娘的衣袖，所以 scale 从 1 调到 0.75（C-02）。verify：剧情文字 237/237 通过，19 FAIL / 7 WARN。备份文件为 scratchpad/index.before-portrait-swap.html。
33. 2026-11-06 Scene 6 后半段按用户指定换图：38 侧门（Old Woman 的 “The ancestral hall suddenly falls silent…”、“The side door…”、“Only now…”）→ 40（You，舞台提示 “You turn to Master and Madam Chen.”）→ 42（Master Chen “How can…” → You “But he is already dead!…” → Master Chen → 收尾段分组 + 选项）。用户上一轮把 Old Woman 这句放在 35，这一轮把它写进 38 那段，按最新说法放在 38。用自然速度走了这一段（约 110 秒），底图高度 680；选 B 进入卡片结果页，结局变量为 C；控制台无报错。verify：剧情文字 237/237 通过，19 FAIL / 7 WARN。备份文件为 scratchpad/index.before-scene6-second-half.html。
34. 2026-11-06 剧本更新（11:45）：Scene 6 A 结果删除 “You slowly set down the teacup.”，已同步到 opts。
35. 2026-11-06 Scene 6 收尾和 A/B 结果：
    - 收尾 “You finally understand…” 换到 女主被喂药，A/B 选项也在这张图上。
    - A：女主披上红盖头（You have pleaded…）→ 女主被放进棺材（You say nothing more.）→ 47B_额间点朱砂、活女主和男主在棺材里（这两张没有文字，各停留约 5 秒）→ 合上棺材（As they lead you…）→ 文字读完后画面在 5 秒内变黑 → Reveal the ending。
    - B：49B_茶杯摔碎：You “No! I will not!” → 旁白 The teacup shatters… → Master Chen（舞台提示 “Master Chen shouts angrily,”）→ 旁白 Several people block your way. → 50B（You struggle…）→ 51B（Your resistance has failed…）→ Reveal the ending → 结局。
    - 播放器新增两个可选字段：bg 步骤的 `hold`（毫秒，无文字画面不加蒙版，见 D-F14）；end 步骤的 `black`（文字读完后变黑，见 D-F15）。
    - 用自然速度走过 A 和 B；verify：剧情文字 246/246 通过，19 FAIL / 7 WARN。备份文件为 scratchpad/index.before-scene6-results.html。
36. 2026-11-06 Scene 6 A 的顺序按用户同意调整：剧本文字没有改，只调整了文字和底图的对应。现在是 女主被放进棺材（You say nothing more. → As they lead you toward the coffin, you simply gaze at the distant sky.）→ 47B、棺内（无文字）→ 合上棺材（This is the last time you will see daylight.）→ 变黑。用自然速度走了一遍（约 45 秒）。verify：剧情文字 247/247 通过，19 FAIL / 7 WARN。备份文件为 scratchpad/index.before-s6a-order.html。
37. 2026-11-06 结局和 Final Screen 改为图片序列（`endings.*.film`、`final.film`；`rbEndPage` 的按钮抽成 `rbEndBtns`，`rbFilm` 用 endA / endCF 这样的进度键）。
    - Ending A：延续 30 → 放进棺材 → 53。Master Chen 这句用对话框，舞台提示 “Master Chen says,”。
    - Ending B：全部在 52 上。
    - Ending C：49B（The teacup shattered…）→ 重复 Scene 6 A 的 5 张图，每张配一句 C 的文字 → 合上棺材后变黑（与 Scene 6 A 一致，用户没有明确要求，需确认）。
    - Final Screen：55 → 54 → 56（后面 3 段和 THE END）。THE END 保留金色和宽字距。
    - 变黑之后下一段从黑场开始，不会闪回上一张图。verify 的序列结构检查也覆盖了结局。
    - 测试：A（接 Scene 5 B）、B、C 都用自然速度走完；A 接 Final Screen 完整走完；C 接 Final 确认从黑场开始；Final 中途刷新能恢复；控制台无报错。verify：剧情文字 256/256 通过，19 FAIL / 8 WARN（新增的 WARN 是 54 有 3.3MB）。备份文件为 scratchpad/index.before-endings.html。
38. 2026-11-06 What If 按用户截图修改（D-L7）：Debate 01/02 改红嫁衣的内容；Debate 03 移到结尾共用页（`renderMethod`）。标注图上写的是 “Education backgrouod”（拼写错误），用户消息写的是 educational background，这里用 “Educational background”。已测试：红嫁衣和 Mohini 的 What If、共用页的 Debate 03、刷新恢复、旧存档的选项值回到默认项；控制台无报错。verify：剧情文字 256/256 通过，19 FAIL / 8 WARN；新增 2 项检查。备份文件为 scratchpad/index.before-whatif-edit.html。
39. 2026-11-06 用户说“都要改”，处理了 What If 的后续：Mohini 的 Debate 01 和红嫁衣相同；“Who knows?” 大写；开头页和 What If 页改为 “two questions”；页底说明只在 Mohini 的 What If 上显示；Debate 03 inter 的红嫁衣文字改为 “money and education”。Debate 03 仍保留在结尾共用页（图 5 的批注）。浏览器里逐项检查了两条线，控制台无报错。verify：剧情文字 256/256 通过，19 FAIL / 8 WARN。备份文件为 scratchpad/index.before-whatif-followups.html。
40. 2026-11-06 红嫁衣开场（D-F16）：新增 `opening` 页。已测试：角色页点进来后全屏（窗口大小 = 画面大小），5 秒显现；按空格后淡出，由黑场接 Prologue；点击也能进入 Prologue；刷新后停在开场页；控制台无报错。窗口接近正方形时图片两侧会被裁掉。画面上没有点击提示（用户要求不显示文字）。verify：剧情文字 256/256 通过，19 FAIL / 7 WARN（Opening 那条 WARN 已消除）。备份文件为 scratchpad/index.before-opening-image.html。

## 待解决问题（需要用户决策）
- [x] **Q1 剧本升级到 V3（剧情文字部分）**：2026-11-04 已同步；理论框见 Q3。
- [ ] **Q1b Final Screen 的样式**：V3 最后一句 “In life, she could not escape…” 暂时沿用收尾样式（斜体加金线）；V2 的 coda “She could resist the marriage…” 在 V3 中没有，已删除。要不要调整？
- [ ] **Q2 V3 的 Opening**：开场画面已完成（D-F16）。“Opening Cultural Note” 要做成可选的信息按钮吗？BGM 要不要加、用什么音频？
- [ ] **Q3 理论框**：V3 每一幕开头都有 “Theoretical Connection | …”，要显示吗？放在哪里（幕开头，还是选择之后）？
- [ ] **Q4 V3 的舞台提示**：Scene 1 A 的 “(Interrupting immediately)” 暂时按 D-T2 放进父亲最后一句的舞台提示行。要不要再加“打断”效果（比如女孩的 “But…” 打字中途被切断）？
- [ ] **Q8 小问题（不影响玩家）**：预览窗口被隐藏时，图片序列会停在“同图无缝衔接”这一步，窗口重新可见后才继续（因为 requestAnimationFrame 在后台会暂停）。需要的话可以加一个定时器兜底。
- [ ] **Q5 结尾总结**：V3 Final Screen 之后的总结段落（“You have reached the end of the story…”）要不要显示？放在哪一页？
- [ ] **Q6 介绍页和档案页**：要不要改成 Phoenix (2006) / 交叉性的框架？
- [ ] **Q7 图片体积**：交付前要不要压缩底图（04、06、08B、09B 都超过 3MB），或者把图片嵌进 html？
- [x] **Q9 Scene 2 的 B 结果**：2026-11-05 已完成。
- [ ] **Q11 Scene 2 B 的地点和时间名称**：The Village Edge、A Fork in the Road、Dusk、The Village、Nightfall、Your Bedroom 是 Claude 拟定的，需要用户确认。
- [x] **Q13 Scene 3 的 B 结果**：2026-11-05 已完成。
- [ ] **Q14 阿月的立绘是微笑表情**：16A 说 “I am sorry…”（含泪）时表情不符，要不要补一张含泪或难过的阿月立绘？
- [x] **Q15 Scene 3 A 的收尾**：2026-11-05 用户决定从 “You walk home alone.” 开始换成 11B 夜晚返村底图（Place 为 The Village）。Time 保持 Three Days Before the Wedding；剧本没写夜晚，所以没改。
- [x] **Q16 Scene 4 A 的收尾**：“Early the next morning…” 目前显示在 20A（梳头）底图上，Time 仍是 The Day Before the Wedding。要不要把 Time 改成 The Wedding Day 或 The Next Morning？要不要换一张底图？
- [x] **Q17 图片序列中间的标签**：`Stage · Place` 标签固定用这段序列的第一个地点。换地点之后，再出现的旁白上仍显示原来的地点（例如 Scene 4 B 在卧室的收尾仍显示 “Scene 4 · The Li Family Kitchen”；Scene 2 B、3 A、3 B 也有同样问题）。要不要让标签跟着 Place 变？
- [x] **Q18 新娘装立绘**：从 Scene 5 开始，女主穿红嫁衣（28 还盖着盖头），但对话立绘仍是蓝布衣的 主角_半身。要不要补一张穿嫁衣的女主半身立绘，用在 Scene 5、Scene 6 及之后？
- [x] **Q19 档案页是否保留**：Amnesia Archive 仍是 Berlant & Warner 框架，和新开头的 Phoenix (2006) 不一致。保留在结局和 What If 之间，还是去掉？
- [ ] **Q20 新页脚**：页脚写的是 “Complete Storyline V2”，目前剧本是 V3。要改吗？
- [x] **Q21 Scene 6 的老妇人立绘**：底图 33–35 里的老妇人是灰发髻、紫褐上衣，而立绘是头巾拄拐的村里老妇人，同时出现时看得出是两个人。要不要补一张祠堂老妇人的立绘？
- [x] **Q22 Scene 5 A 的女主立绘**：现在有嫁衣立绘了，要不要把 28 上 “As long as I am alive…” 的蓝布衣立绘换成嫁衣立绘（Q18）？
- [ ] **Q23 Scene 6 的 42 底图**：42 里女主嘴被布堵住、被两名女仆抓住，但这张图上她还要说 “But he is already dead!…”，之后的选项还要 “set down / knock over the teacup”；分镜文档也写过堵嘴不在剧情内。要不要改图，或调整这张图开始的位置？
- [ ] **Q24 Scene 6 的 Old Woman 这句**：放在 38 上时，侧门和棺木在 “The side door…slowly opens” 之前就已经出现。要不要把这句放回 35，从 “The side door” 开始换 38？
- [x] **Q25 What If 的引导文字**：What If 页写着 “explore three questions”，开头页写着 “three questions drawn from the reading”，但现在 What If 上只有两个 debate；页尾说明还提到 sexuality / gender，红嫁衣线已经没有这两项。要改吗？
- [x] **Q26 Mohini 的 Debate 01**：标题和选项要不要也按红嫁衣的改？
- [ ] **Q12 Scene 2 A 的收尾**：A 线的 “You lie awake all night…” 仍然显示在 07B 厨房（白天）的底图上；要不要也换成 12 窗边未眠？
- [x] **Q10 顶部信息栏**：2026-11-05 用户决定 Place 和 Time 都随画面变化（D-F11）。目前只有 Scene 2 A 的收尾改为 That Night。

## 下一步
1. 等用户对 Q1 做决定，再同步 V3 文字（只改用户点名的部分）。
2. 继续按 decisions 里的 F 系列原则为 Scene 2 及之后的场景做图片序列（需要用户提供底图和立绘）。
3. 每完成一项都运行 `python3 verification/verify.py`，并更新本文件。
