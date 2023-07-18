data = {
    'start_message': """欢迎使用ChoiceMaster！🤖
有时很小的选择也会耗费我们大量的能量，借用工具来减少在选择上消耗的心力和时间吧。
我是一个帮助你做决策的机器人。以下是我的命令列表：

/yesorno - 随机回答是或否的问题。
/random - 生成[num1,num2]之间的随机数。
/dosth - 给你一些建议，让你做点什么
/choose - 输入你的选项，我来帮你选择
/mindfulness - 正念的力量
无论你需要做抉择、获取随机数还是找到下一步的活动，我都会尽力帮助你。

你也可以试着向我提问题，不过最重要的是遵从你的内心。

祝你好运！✨""",

    'YES_NO': ["YES", "NO"],

}
activities_long_term = [
    '看书📘。可以获得新的知识和视角',
    '爬山🧗‍。远足可以锻炼身体,享受大自然',
    '游泳🏊‍。水上运动可以舒缓压力',
    '游乐园🎠。找点刺激放松心情也不错',
    '动物园🐯。近距离接触动物很有意思',
    '整理房间🛏。环境整洁有助于心情愉悦',
    '逛博物馆🏛。了解新的事物和历史背景',
    '如果是白天,出门逛逛🚶‍️。走一条从未走过的路线。转变环境',
    '健身🏋️‍。适当运动对身心都有益',
    '冥想🧘‍。让心智沉静下来',
    '追剧📺。放松心情是必要的',
    '看电影🎥。进入另一个世界',
    '去逛超市🏬。逛商场,菜场也可以。看看琳琅满目的商品和人间烟火气',
    '唱歌🎤。尽情表达自己吧',
    '天气好的话去骑自行车🚴‍。穿行于街头',
    '打游戏🎮。偶尔娱乐一下没问题',
    '逛公园🌲。享受大自然,呼吸新鲜空气',
    '洗衣服🧺。完成家务也能带来成就感',
    '洗澡洗头发🛁。慢慢吹干,然后顺毛。哪个小动物不喜欢顺毛呢?',
    '逛街🛒。购物是一种放松',
    '阅读📖。获得新的视角和知识',
    '出门随意地走走看看🚶。放空心情',
    '烹饪🍳。做出美食也很有满足感',
    '背单词📓。增长一个词汇量',
    '搞卫生🧹。让环境更加整洁',
    '做一组拉伸运动🤸‍。活动活动身体',
    '坐一趟没有目的的公交🚌。看看风景,听听人世间,享受独处又安全的时光'
]
activities_short_term = [
    '写下今天令你感到幸福的三件事吧~🥰。记住快乐瞬间',
    '简单收拾一下床铺🪄。一床整洁被窝能带来好心情',
    '洗衣服👚。再认认真真地晾晒🧺。洗衣服会让房间更加整洁',
    '在房间内随意地走动 🚶‍。适当活动可以放松身心',
    '阅读📖。看看喜欢的书,获取知识也能放松',
    '听音乐🎧。让优美的音乐陪伴',
    '简单收拾一下房间🧹。整理环境能让人心情明朗',
    '你喜欢唱歌吗?如果一个人的话放声哼几句你喜欢的歌吧。不用在意走不走调。\n唱歌🎤是一种无害的发泄情绪的方式,还能让我们保持有节奏的、更深的呼吸,为大脑提供更多氧气。',
    '做简单的拉伸🤸‍。伸展一下身体可以放松肌肉',
    '在纸上写下📝让你感觉快乐和感恩的三件事情。追踪幸福源泉能带来正能量',
    '到楼下的商场或小卖部逛一逛🛍。看一看,买些好吃的。换换环境,获得一些小惊喜',
    '吃点零食🍿。偶尔犒劳自己一下没关系',
    '扔掉一件没有用的东西🗑。清理环境可以提升心情',
    '听播客🎙。获取新的信息也是一个不错的选择',
    '站立背单词📚。一些小学习可以让大脑保持活跃',
    '去找喜欢的人说说话(包括你的朋友和亲人)💬。聊聊天能获得支持',
    '洗碗🍽。完成一些小任务会带来成就感',
    '去丢垃圾🚮。整理干净环境很有必要',
    '整理电脑桌面💻。让工作区域井井有条',
    '整理你的工位。让工作区域井井有条',
    '涂上喜欢的口红💄。看见镜子里好气色和美丽的自己。',
    '做一做颈椎操💪。舒展一下颈部肌肉',
    '吃点或喝点东西🍔。补充一下能量',
    '玩会社交软件📱。看看沙雕网友们在干嘛',
    '站立拉伸🧘‍。可以活动活动身体',
    '站立冥想💆‍。集中注意力到呼吸上',
    '买杯奶茶/可乐/果汁🥤。犒劳一下自己',
    '站起来扭一扭身子👋。伸一伸懒腰🤹‍。活动一下身体,缓解久坐的疲劳',
    '站起来闭目养神🧘‍。轻松地调整一下呼吸,让大脑放松一会儿'
]
replies = ['慢下来。', '烦恼快要消失。', '善待自己。', '对读一本书。', '回头看看。', '逆水行舟。', '相遇。', '放轻松这很简单。',
           '早点儿开始。',
           '站在最重要的地方。', '不要后悔。', '最美丽的一天。', '背不动的就放下。', '必须努力奔跑起来。', '学会改变什么。', '成为了事实。', '会被一直依赖的。', '骗不了自己。', '回家。',
           '不要一成不变 。',
           '挥别错的。', '时间有限。', '把握现在。', '轻而易举的伤害。', '慢些，我们会更快。', '平凡之路。',
           '扔掉这 些东西。', '不要刻意压抑。', '没有答案。', '最后什么都没改变。', '等待。', '驾驭。',
           '下一页才是你人生的答 案。', '多余。', '不要害怕做出任何决定。', '捕风捉影。', '你失去的某一天会以不同的方式归还于你。', '取暖。', '你无法继续沉睡。',
           '不要给人添麻烦。',
           '让你泪流 满脸的。', '其实大家都知道。', '这不是能犹豫的事。', '试着安静一会儿。', '抱抱你自己。', '显得有点唐突。', '安静。', '萌芽。',
           '永远不会愈合的伤口。',
           '下一个天亮。', '用平淡的心态去追求。', '你祈求的一切顺利。', '直面残酷。', '学会珍惜。', '岁月静好。', '去爱。',
           '不必为你无法控制的事情担心。', '远行。', '戒掉过分的急躁。', '告别。', '别失望。', '有一些重要的事。', '得到了多数支持。', '一切顺其自然。',
           '孤单。',
           '也许会有好转 。', '一直走下去。', '轮回。', '完美时刻。', '浪费光阴。', '学会好奇。', '复杂的事情简单做。', '你会忘记它。', '有点儿心疼。', '保密。', '差不多得了。',
           '得不到别人的认同。',
           '促足静立。', '给自己一个肯定。', '暂且不要判断。', '找回自己。', '一成不变。', '寻寻觅觅。', '一条没有鲜花的道路。', '你大概会受伤点。', '盛开。', '奇迹。',
           '种下满足，收获幸福。',
           '自我欣赏。', '一个人细水长流。', '学会自己保护自己。', '十分好的预感。', '对未知前途的期盼。', '自信来吧。', '没有什么是对的。', '改变心情。',
           '会有人陪着你。'
           '一切皆有可能。', '退后一厘米。', '不要怕。', '这真是一个奇怪的问题。', '出发。', '停止。', '唤醒沉睡的你。', '试着慷慨一点。', '给人依赖。', '到此为止。', '也许会到。',
           '不要看轻别人。', '常常是最后一把钥匙打开了神殿门。', '了不起。', '放手。', '结束倒计时。', '不知所措。', '呼吸一下新鲜空气。', '好天气。', '成长。',
           '学会认错。',
           '可以期待的未来。', '悄悄躲开。', '未解之谜。', '没什么放不下。', '或许需要突破。', '享受全心全意的付出。', '控制自己的情绪。', '阳光。', '爱。',

           '你唯一能做就是把握现在。', '不要刻意隐藏。', '对，去吧。', '有人浪费你的时间。', '迷人的危险。', '不要忘记微笑。', '糊涂一点更好。', '坚强。',
           '挥手道别。', 'trust no one, trust code',
           '一个正在到来的晴天。']
sleeps = ['睡眠是身体最好的修复神器。', '我的身体让我感到强壮和自信。']
mindfulness = ['不为没发生的事提前焦虑,不为别人的想法惩罚自己。', '我是来享受人生的，不是来长结节的。', '你要知道除了生病以外，你感受到的痛苦都是你的价值观带来的，而非真实存在。',
               '内心一旦平静，外界便鸦雀无声。',
               '当你厌恶身边人时，自己加把劲远离他们', '不要因为别人发光，就觉得自己暗淡。每个人都活在自己的节奏里，自顾自地往前走吧。', '想太多会让你变得敏感而焦虑，很多事没你想的那么严重。',
               '如果有人诋毁你，那是在替你消灾！如果有人针对你那是在替你挡祸！', '提醒自己：想是问题，做是答案',
               '不要总是说烦死了、累死了、完了。不仅被人轻视，而且越讲越走不出来。要多说没事、问题不大、可以解决，养成说好话的习惯会提升你的运气。',
               '顺其自然，时间会给你答案。', '有的人挑你毛病，只是想立威，而不是你真的有毛病。', '不用总是纠结你的出生怎么样、长得怎么样。除了这些，你还有脑子和时间，你可以不断进化自己。',
               '你最大的资本其实就是你自己。', '你心态好，你就可以搞别人心态。你心态不好，你就只能被别人搞心态.', '并不是所有人都值得你真诚对待，你的善良必须带点锋芒，才能更好地保护自己。',
               '亲爱的女孩，别畏手畏脚的。大胆点，去做你想做的事！', '我从我的努力中获得乐趣，即使是最平凡的努力。', '当我呼吸时，我吸入自信，呼出胆怯。',
               '我总是被爱所包围，宇宙的爱 ，人类的爱，小动物的爱，大自然的爱。',
               '今天，我不再担心问题，而是寻求解决问题的答案。', '没有任何人、任何地方、任何东西能对我发号施令，我是自由的。', '我投入时间和精力来改善我的生活。', '我对所拥有的一切心怀感激。',
               '我是一个聪明的人，我会做出正确的决定。', '我坚韧不拔，但我也应该得到休息。', '停下来也没关系,我正在恢复能量。', '我值得享受这个世界。',
               '我有力量度过任何难关。', '我为自己所有大大小小的胜利感到骄傲。', '我正在尽我所能，我也乐在其中。', '我的想法和感受很重要。', '我和我的过去和解，因为是他造就了现在的我。',
               '我所度过的每一个艰难日子都向我揭示了我的力量。', '我会放下令人不安的能量，转而拥抱平和的能量。', '今天是非常适合感受快乐的一天。', '每一天，我都在自我疗愈和自我提升的轨道上前进。',
               '我爱现在的自己，也爱我正在成为的那个人。', '不管我被置于何种境地，我都是个很棒的人。',
               '我知道，我是为了当下的生命体验而来。在每一个当下，我唯一要做的，就是完全地允许、充分地经历、彻底地体验、尽情地享受。静静地看着，只是看着，然后，允许一切发生。',
               '我能适应生活中发生的任何变化。', '现在的我足够好、足够聪明也足够强大，以后也会是。', '我会吸引我所提到的东西，所以我只说积极的话。', '我允许自己享受人生。', '我只需要获得自己的许可。',
               '我拒绝让自己在追求“美好生活”的过程中痛苦不堪。', '我是平静、快乐、健康的，我可以自由地做我自己。', '我所经历的一切都在我心中埋下了珍贵的种子。', '我很高兴我拥有自信和明确的自我意识。',
               '我接受自己无法改变的东西，并会找到勇气去改变我能改变的东西。', '一个人活在今天，只要把今天的地扫干净、把今天的心扫干净就行了，因为明天有明天的心和明天的落叶。',
               '我迈出的每一步都让我的力量增强。', '我允许爱流入我的世界。', '我会无条件地爱自己。', '我拥有独一无二的内在力量。', '我拥有独一无二的内在力量。',
               '无论外界是否认同我，我都觉得自己很安全。', '我全然地接纳真实的自己。我不再相信自己创造出来的内在恐惧。', '我允许自己可以脆弱，我允许自己可以柔软。',
               '我可以去犯错，因为这是成长的一部分。', '我用充满爱的目光注视自己，我爱我所看到的一切。', '我不再纠结自己本应做到的事，而是采取行动，做我现在可以做的事情。',
               '每个人都有自己特定的人生课题。我不再比较，也无需比较。', '我原谅自己过去所有的错误和失败。今天是一个崭新的开始，我和过去的那个自己勇敢说再见。',
               '我吸入信心，呼出疑虑。我允许自己放下、放松、保持冷静。',
               '即使在困难时期，我也选择看到生活中的美好。', '我接纳并爱护真实的自己。', '正在调整心态，一切都会非常顺利的。', '我可以感到脆弱、敏感和悲伤。我允许自己休息一段时间。',
               '每迈出新的一步，我都会大声称赞自己。', '如果我想得到我从未拥有过的东西，就必须去做我从未做过的事。', '我为自己做出积极的选择。', '有些事情是我无法改变的，我对此释怀。',
               '照顾好自己是我的首要任务。', '在艰难的日子里，我把所有的精力都留给自己。', '我带着对健康的憧憬去积极疗愈我的身体和心理，并相信一切都会好起来。', '今天和往后的每一天，我都选择快乐。',
               '我允许自己不加评判地做我自己。', '不管发生什么事，我都能应付。', '所有的障碍都是为了帮我找到真正属于我的路。', '宇宙正在秘密做着对我有利的事情。',
               '我觉得现在的自己很好，也会爱我正在成为的那个自己。', '我专注于积极的进步，无论是大是小。', '我会从脑海中消除所有的自我怀疑，我拥抱希望、快乐和勇敢。',
               '我愿意为了更好的自己而改变。', '每向前迈出一步，我的信心就会增强一分。', '我的生活由我掌控。', '我冷静、平和、专注。', '我是一个强大的人，充满了希望、信心和热情。',
               '我会变得更开明，更少去评判他人。', '我会利用这些艰难的日子来成为一个更好的人。', '我为自己努力尝试感到骄傲。', '我专注于积极的想法并期待积极的结果。',
               '我感恩此刻生命里我所拥有的一切。', '我会无条件地爱自己。我允许爱流入我的世界。', '我对自己有耐心，我明白积极的改变需要时间。',
               '被打倒没什么大不了，我会一次次重新站起来。', '我对拥有健康和精力心怀感激。', ]
