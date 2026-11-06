# 已确认的制作决定（decisions）

这里记录用户确认过的交互和制作方式，作为以后可以反复套用的**通用原则**。
新内容追加在对应分类下，编号顺延。用户推翻某条时，要标注“已废止”并写明替代条目，不要直接删除。

---

## 一、文案（T）
- **D-T1 唯一来源**：剧情文字严格按 `最新版本文案/` 里的英文剧本，逐字使用（多次强调）。
- **D-T2 允许的拆分**：可以在句子边界把长段落拆成多步；`Name: “…”` 拆成名牌加台词；`X calls/says:` 这类引导语留作旁白（保留原文冒号），引出的话放进对话框；夹在台词前面的动作描写（如 “Your father frowns.”）放进对话框的舞台提示行（灰色斜体）。
- **D-T3 用户指定的例外**：序章 B 的旁白截成 “You step softly toward the door.”（原文后面还有 “and hear your father say,”）。
- **D-T4 名牌**：Mother / Father / You 直接取自剧本；运粮男人的名牌是 “A Man”（用户确认）。剧本没有 `Name:` 时，可以用剧本正文里原样出现的称呼（例如 “A-Yue”“A-Yue’s father”），但不能自己起名（C-03）。
- **D-T6 括号里的舞台提示**（如 “(Interrupting immediately)”）按 D-T2 处理，放进下一句台词对话框的舞台提示行，保留括号（2026-11-04 首次使用，具体呈现方式待 Q4 确认）。
- **D-T7 Mohini 线**（2026-11-06，用户要求）：文字来源是 `印度故事/Mohini Pei- Summary (1).pdf`，格式和红嫁衣的卡片页相同（Place/Stage/Time 栏、打字机、底部选项、结果另起一页）。只放 PDF 标为 on-screen 的内容，以及 Dialogue、选项和结局。Transition、Visual and audio cues、Intersectional significance 是制作说明，不显示。on-screen question 放在正文最后一段（`rb-em`）。Place/Time 取自每幕的 Setting。PDF 里是直引号，按原文保留。不再使用旧的数值条和 Berlant 理论框。例外：用户指定 Scene 1 的 Transition 第一句 “The palace becomes a recurring presence in Mohini's life.” 在三个选项之后都显示；Scene 2 的 “The king's letters become less frequent.” 同样如此。规律：每幕三个选项都收束到 Transition 的第一句和用户指定的底图。Scene 3 及之后由用户逐幕指定。
- **D-T8 Mohini Scene 4 裁剪**（2026-11-06，用户要求）：开头一句只保留 “The king's final letter arrives.”（PDF 原句后半 “without a signature: there will be no marriage.” 删除，信上的图已写明），`verify.py` 的 `MOHINI_ALLOW` 白名单里有这一句；“Your father has barred the gate, hoping the gossip will pass.” 之后的 “The room is full of people who love you.” 和 “It has never felt so lonely.” 删除。三个选项之后共用 PDF 的 Transition 句作收尾，配 Scene4_10 和 Scene4_09。
- **D-T9 Mohini 删句**（2026-11-06，用户要求）：Scene 5 选项 C 删掉 “Your friend remembers every word, even when the public story changes.”；Final Scene 删掉 “ENDING UNLOCKED: The Woman the Village Forgot” 和 PDF 标为 Required on-screen note 的说明文字。Final Scene 现在以引语 “He returned to his palace…” 结尾。
- **D-T10 图片翻译**（2026-11-06，用户要求）：`00_开场` 最下面加 “[translation: Spirit Tablet of Mr. Chen]”；`52_结局` 加 “[translation: Spirit Tablet of Mr. Chen; Spirit Tablet of the Wife of Mr. Chen]”。两处颜色都是 #e8d8a6（偏黄）。配置在 `RB_NOTES`，用图片坐标定位，原图不动。52 放在水平居中的供桌前沿，不放在图片正中，因为正中是灵位和旁白。
- **D-T5 剧本路由提示不显示**：“→ Proceed to Scene 6”“Only players who chose…” 这类提示只用于分支逻辑，不作为文字显示给玩家。

## 二、页面布局（L）
- **D-L1 剧情卡片**：顶部是 Place / Stage / Time 栏（Stage 高亮），下面一张卡片：小标签 → 标题 → 横线 → 正文 → 底部选项（虚线框）。沿用原 html 的暗色调、衬线字体和金色强调色。
- **D-L2 逐步显现**：文字用打字机效果或逐句淡入淡出，**文字结束后才出现选项**；点击或按空格可以跳过当前动画。
- **D-L3 结果另起一页**：选择之后不在原页展开，而是换成新的一页，结果文字出现在原来正文的位置，不再保留选项。
- **D-L5 刷新后停在原处**（2026-11-05，用户要求）：整个游戏状态保存在 sessionStorage（键为 `monsther-state`），刷新后恢复到原来的页面。图片序列会从当时那一步、那一句对话继续，底图、Place、Time 一起恢复；已经到达结尾画面的，刷新后直接显示结尾和选项。卡片页刷新后从头重新打字。只在当前标签页内有效，关闭标签页或新开标签页会从头开始（如果要跨会话保存，改用 localStorage）。Mohini 线同样适用。
- **D-L6 开头和结尾页来自新版 html**（2026-11-06，用户要求）：`monsther_final_story_experience.html` 的开头、角色选择、What If、What If 下一页已移入 `index.html`（`mhPages`，样式都限定在 `.mh` 下，不影响故事页）。
  - 开头：图 1 红框换成用户给的段落 “From an intersectional perspective…”；图 2 的 “Choose a story →” 已删除；唯一的内容按钮 “Discover the project →” 进入角色选择页。
  - 角色选择页：点击后进入原有的 Mohini / 红嫁衣故事。
  - 结尾（两个故事相同）：结局页的按钮改为 “Ask: What if? →” → What If 页 → 共用页（Explore the other story / Return home）。红嫁衣线这个按钮在 Final Screen 上；Mohini 线在她的结局页上。
  - 2026-11-06 用户决定：档案页（Amnesia Archive）整页删除；首页不显示 Return home，其他新页面保留。
  - 这些页面的文字来自用户提供的 html，不属于剧本，按原文保留。What If 的三个选择会存在 `state.wi`，刷新后恢复。
- **D-L7 What If 内容**（2026-11-06，用户在截图上标注）：
  - Debate 01（两条线相同）标题为 “What if she could get different support?”，只保留 Independent financial resources 和 An ally with institutional influence。
  - 红嫁衣 Debate 02 只有 Economic position 和 Educational background，解释文字是用户原话（用户同意把 “who knows?” 改成 “Who knows?”）。
  - 两条线的 Debate 03 都从 What If 移到结尾共用页，放在总结文字下面、按钮上面。
  - Mohini 的 Debate 02 未改。
  - What If 页和开头页都写 “two questions”。
  - 页底说明 “These speculative stories…” 只在 Mohini 的 What If 上显示。
  - Debate 03 的 inter 解释：红嫁衣写 “money and education”，这个措辞由 Claude 改写，用户同意修改、但还没看过具体文字；Mohini 保持 “money, community ties and recognition”。
- **D-L8 第二篇文献**（2026-11-06，用户要求）：首页 Phoenix 卡片下面加 Nina Lykke (2010) 卡片，文字是用户原话；页脚加 “Second theoretical source: Lykke, N. (2010)…”。页脚里的出版社 Routledge 和章节标题的句首大写格式是 Claude 补的，用户还没确认。
- **D-L9 首页文献排版**（2026-11-06，用户要求）：说明文字横向铺满，两篇文献卡片在下方并排；手机宽度下上下排列。
- **D-L10 不留单词行**（2026-11-06，用户要求）：剧情文字换行时最后一行不能只有一个单词，也不能靠合并句子解决。旁白、问题和选项用 `text-wrap:balance`；旁白、对话、结尾文字显示时用 `rbGlue` 把最后两个单词用不换行空格连住（只影响显示，`data` 里的文字不变）。
- **D-L11 进度条**（2026-11-06，用户要求）：Place/Stage/Time 面板顶部有可点击进度条，节点文字和悬停标题取自现有 Stage 和场景标题。红嫁衣 11 个节点（Prologue、Scene 1–6、Ending A/B/C、Final Screen），Mohini 6 个节点（Scene 1–5、Final Scene）。只有玩过的节点能点，未玩过的节点变暗、不显示标题；玩完后可以点回玩过的章节。往回跳和 Replay 不重新上锁。跳转从该段开头播放，往回跳时清掉该段及之后的选择记录。解锁记录在 `state.seen`，随 sessionStorage 保存。手机宽度只显示圆点。
- **D-L12 结尾页文字**（2026-11-06，用户要求）：`reflect` 页原来的 “Her identity did not determine her fate…” 换成用户给的 5 段文字，两个故事共用。滑动时文字固定，每滑一段距离浮现下一段，已浮现的保留，滑到最后 5 段全部显示。屏幕太矮放不下时直接全部显示。
- **D-L13 页脚文献**（2026-11-06，用户要求）：Phoenix 和 Lykke 改成 APA 7，标签和其他句子不变。Crossref 记录没有 Phoenix 的卷号，所以只写期号 (2–3)。Lykke 是单一作者的书，按 APA 引用整本书，章节信息保留在首页卡片上。
- **D-L4 结局与 Final Screen** 使用和剧情页相同的卡片排版；结局之后进入 Final Screen，再进入 What If（档案页已于 2026-11-06 按用户要求删除，见 D-L6）。

## 三、图片序列 / 镜头（F）——新增画面时默认按这套做
- **D-F1 只覆盖卡片区域**：底图只铺满剧情卡片，卡片高度固定，各场景的底图尺寸保持一致。
- **D-F2 开场**：底图从黑场慢慢浮现，同时轻微推近 → 叠上灰色蒙版 → 旁白一句句在画面中央淡入、停留、淡出。
- **D-F3 节奏**：不点击就按原速自动播放（停留时间随句子长短变化）；点击或按空格大约 0.4 秒切到下一句；正在打字时点击会先把这句显示完整。
- **D-F4 对话段**：灰色蒙版变淡，半身立绘从左侧滑入左下角，右侧对话框（金色名牌）用打字机效果显示台词；换人时先滑出再滑入。对话结束后蒙版恢复。
- **D-F5 结尾**：最后一句旁白留在画面上，底部出现选项（选择前）或 “Continue →”（选择后）；底图和蒙版保持不变。结尾没有文字时只显示按钮。
- **D-F6 换底图**：同一张图之间无缝衔接；不同图之间交叉淡化（蒙版先退开，新图停留片刻，再盖回蒙版）。
- **D-F7 Skip**：只跳过对话，落在收尾旁白上；收尾段落不能被跳过，播放期间隐藏 Skip。
- **D-F8 中间标签**：格式为 `Stage · Place`（如 “Scene 1 · The Courtyard Gate”）。2026-11-05 用户同意：标签的 Place 部分跟着顶部 Place 变化（`rbSetPlace` 会同时更新标签；刷新恢复时也一样）。换地点后的旁白上显示新地点。
- **D-F10 底图上的旁白要拆成短句组**（2026-11-04，用户提出“段落太长、看着吃力”）：播放器自动在句末断开，每组大约 120 字以内；单句超过 140 字时，也可以在冒号或分号后断开；引号里面的话不拆开。同一段内各组之间的间隔较短（0.9 秒），段与段之间 1.4 秒。end 段的前几组依次显示，只有最后一组留在画面上，和选项或按钮一起出现。剧本原文数据不改，拆分只影响显示。
- **D-F11 Place 随地点变化**（2026-11-05）：顶部 Place 跟着画面里的实际地点走。换到新地点的底图时，在那个 `{bg}` 步骤里写上 `place`，播放到这张底图时 Place 就会更新；没写 place 的底图沿用这一幕的地点。已有的值：05 床边是 Inside the House，07A/07B 厨房是 The Li Family Kitchen。地点名称属于 UI 文字，新地点要先报给用户确认。
  **Time 同理**（2026-11-05，用户决定）：任何步骤都可以写 `time`，播放到这一步时更新顶部的 Time（Skip 跳到结尾时，采用最后一个写了 time 的值）。已有的值：Scene 2 A 收尾 “You lie awake all night…” 是 That Night；Scene 4 A/B 收尾 “Early the next morning…” 是 The Wedding Day（2026-11-05 用户同意，沿用 Scene 5/6 已有的值）。命名沿用 “The Next Day” 这种写法；剧本里出现时间变化（例如 night、the next morning）就标出来，并先报给用户确认。
- **D-F12 换底图时不显示中间标签**（2026-11-05）：`Stage · Place` 标签只在这一幕开场时出现；两张底图交叉淡化期间隐藏，等下一句旁白出现时再显示。
- **D-F13 结果段开头沿用原底图**（2026-11-06，用户决定）：选择之后，用户没有指定底图的开头几句，放在选择前的那张底图上（例如 Scene 5 B 的第一句留在 27 上），从用户指定的句子开始再换图。
- **D-F14 无文字的画面**（2026-11-06）：一句话要配多张底图时，文字放在第一张上，后面的图用 `{bg, hold:毫秒}` 不加蒙版、不显示文字，依次切换（Scene 6 A 的 47B 和棺内）。
- **D-F15 变黑**（2026-11-06，用户要求 Scene 6 A 结尾变黑）：end 步骤写 `black:true`，最后一段文字读完后，底图在 5 秒内变成全黑，文字留在画面上，然后才出现按钮。
- **D-F16 红嫁衣开场**（2026-11-06，用户要求）：点进红嫁衣先进入 `opening` 页。`00_开场_纸人围观冥婚.png` 铺满整个浏览器窗口（这是 C-07 “只覆盖卡片”的唯一例外），没有任何文字，从黑暗中用 5 秒显现；点击或按空格后约 2.4 秒消失，再由黑场进入 Prologue。Opening 那段剧本不显示文字，verify 的覆盖度已按此处理。“Replay this chapter” 也会重新播放开场；Mohini 线没有这一页。
- **D-F17 没有立绘的对话**（2026-11-06）：talk 不写 `img` 时只显示对话框，不显示立绘（目前用于 Mohini 线的 Attendant，他没有立绘）。
- **D-F18 一行行浮现**（2026-11-06，用户要求）：`{stack:[句子…]}` 让几行文字依次淡入并留在画面上，全部显示后停留一会儿，再一起淡出；点击可以提前出下一行。用于 Mohini Scene 2 开头。
- **D-F19 Mohini 开场**（2026-11-06，用户要求）：和红嫁衣一样先进 `opening` 页，图片是 `Ending_02_传说中的茉莉幽灵_正面恐怖版_v2.png`，全屏，点击后进入 Scene 1。声音是结尾出走的开头约 5 秒（第 3.8 秒起淡出）。玩家点掉这张图时声音随之结束，之后到 Jasmine 那句才开始开头快乐音乐，两段不重叠（用户要求）。
- **D-F20 翻译文字不重叠**（2026-11-06，用户要求）：翻译文字不能碰到旁白、标题、提示和按钮。碰到按钮时按钮下移；挪不开时翻译在按钮出现前淡出。碰到 “Click to continue” 时隐藏这一屏的提示。有翻译的开场图从底部对齐裁切，保证最下面的区域可见。
- **D-F9 共用收尾段落**（剧本里 “Whichever path you choose…” 这类）：按句子拆成若干旁白，最后一句留在画面上并出现 Continue；理论框和 Continue 一起出现。

## 四、立绘与素材（A）
- **D-A1 半身立绘裁剪方法**：按 alpha 通道找到人物边界，四周留 24px，从头顶裁到人物高度的 52%（母亲是 55%），缩放到高 900px，存成 `原名去掉后缀_半身.png`，放在原图同一个文件夹，原图不改。
- **D-A2 立绘不翻转**，一律从左侧滑入（见 C-01）。
- **D-A3 大小**：默认 `scale` 为 1；会挡住底图人物时调小（运粮男人 0.68，Scene 1 全部 0.75）。
- **D-A7 嫁衣立绘**（2026-11-06）：从 Scene 5 上轿开始，女主用 `女主_嫁衣定稿_半身.png`；祠堂里的 Old Woman 用 `祠堂老妇人_半身.png`，Scene 2 村里的 Old Woman 用 `老妇人_半身.png`。
- **D-A4 换表情**：剧本写到情绪变化时换对应表情的立绘（例如 “Your father frowns.” 之后换成生气的父亲）。
- **D-A5 底图**：16:9（1672×941），放在 `第一章场景/NN_描述_v1.png`，通过相对路径引用。html 必须和素材文件夹放在同一目录下。用户移动素材文件夹后，按用户决定修改 html 里的路径，不要擅自把文件挪回去（2026-11-05：`角色立绘/` 移到了 `红嫁衣角色立绘/角色立绘/`）。
- **D-A6 版本管理**：项目使用 git，远程是 Monica11110702/NMC5369-Gender-media-project（2026-11-05 创建时是私有，2026-11-06 查到已是公开仓库并开了 GitHub Pages：https://monica11110702.github.io/NMC5369-Gender-media-project/），通过 HTTPS 推送（Classic Token 存在钥匙串里；2026-11-05）。只有在用户要求上传时才提交和推送。`.gitignore` 排除 zip 备份、Word 锁文件和 .DS_Store。

## 音频（S）
- **D-S1 红嫁衣音频**（2026-11-06，用户要求）：`红嫁衣音频/` 的文件按句子触发，配置在 `RB_MUSIC`、`RB_FX`、`RB_CUES`、`RB_SCENE_MUSIC`。开场页：开头恐怖音乐（不循环）。“Afternoon sunlight…” 起：红嫁衣-前期。“Why do I not even have the power…” 起：红嫁衣-逃跑。“Early the next morning.” 起：开头or婚礼开始的时候，到结尾。三段背景音乐循环，进入 What If 或离开故事时停止。音效：Your mother seems to be crying（母亲哭泣1）、You lower your head…（母亲哭泣2）、A horse-drawn carriage passes（马车声）、The teacup shatters on the floor（打碎碗）、You struggle with all your strength（女生尖叫）。
- **D-S2 音频行为**（2026-11-06）：背景音乐切换时交叉淡化 1.2 秒。跳转、Skip、刷新都按当前位置决定音乐，同一首不重头播。母亲哭泣1、2 播放时压低音乐（到 20%、50%），因为原音频很轻。刷新后浏览器要等玩家点一下才出声。音量是按响度测量定的。2026-11-06 用户试听后确认音量和时机可以。

- **D-S3 Mohini 音频**（2026-11-06，用户要求）：`印度故事音频/` 三首都循环。“Jasmine is threaded into your hair.” 起：开头快乐音乐。“At the market, conversations stop when you approach.” 起：被舆论淹没。“Mohini leaves the house before dawn,” 起：结尾出走，到结尾。进入 What If 或离开故事时停止。音量 60%、60%、90%。从开头快乐音乐自然进入 Scene 3 时，等到 At the market 这句才切换；从进度条跳到 Scene 3 时直接放被舆论淹没。配置在 `RB_MUSIC`、`MH_CUES`、`MH_SCENE_MUSIC`。

## 五、工程流程（P）
- **D-P1 补丁方式**：先备份 → 用 Python 脚本精确替换（断言替换处只出现一次）→ 断言用到的剧情文字在剧本中逐字存在。
- **D-P2 预览方式**：用 `.claude/launch.json` 的 `game` 本地服务器预览，不用 file:// 打开。
- **D-P3 测试方式**：先用快速脚本检查流程是否走得通，再用自然速度完整走一遍；在用户能看到的预览窗口里测试时，要说明那是测试画面。
- **D-P4 汇报方式**：改了什么、怎么验证的、哪些没验证到、可能的连带影响，然后询问是否继续。
