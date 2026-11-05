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
| Scene 4 | 卡片 + 打字机，没有图片 | ✅ 与 V3 一致（2026-11-04 同步） |
| Scene 5–6 | 卡片 + 打字机，没有图片 | ✅ 与 V3 一致 |
| Ending A/B/C | 卡片 + 打字机，没有图片 | ✅ 与 V3 一致 |
| Final Screen | 卡片 + 打字机 | ✅ 正文与 V3 一致（理论框仍是 V2） |
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

## 待解决问题（需要用户决策）
- [x] **Q1 剧本升级到 V3（剧情文字部分）**：2026-11-04 已同步；理论框见 Q3。
- [ ] **Q1b Final Screen 的样式**：V3 最后一句 “In life, she could not escape…” 暂时沿用收尾样式（斜体加金线）；V2 的 coda “She could resist the marriage…” 在 V3 中没有，已删除。要不要调整？
- [ ] **Q2 V3 的 Opening**：做成开场画面吗？“Opening Cultural Note” 要做成可选的信息按钮吗？BGM 要不要加、用什么音频？
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
- [ ] **Q12 Scene 2 A 的收尾**：A 线的 “You lie awake all night…” 仍然显示在 07B 厨房（白天）的底图上；要不要也换成 12 窗边未眠？
- [x] **Q10 顶部信息栏**：2026-11-05 用户决定 Place 和 Time 都随画面变化（D-F11）。目前只有 Scene 2 A 的收尾改为 That Night。

## 下一步
1. 等用户对 Q1 做决定，再同步 V3 文字（只改用户点名的部分）。
2. 继续按 decisions 里的 F 系列原则为 Scene 2 及之后的场景做图片序列（需要用户提供底图和立绘）。
3. 每完成一项都运行 `python3 verification/verify.py`，并更新本文件。
