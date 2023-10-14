import random
import flask
import json

app = flask.Flask(__name__)

@app.route("/api/quote")
def generate_random_quote():
    quotes = [
        "欢迎来到银河编程 Welcome to GalaxyCode",
        "山重水复疑无路，make后面不加to",
        "想致富，先撸树。",
        "要是追你那么容易，那我爱你干嘛",
        "花开花落终有时，相逢相聚无本意",
        "1+1+4+(5+1+4+1+9-1+9-8-1)x0=6",
        "你干嘛哈哈哎哟",
        "千里之行，始于足下",
        "没有BUG的代码是不完美的！",
        "失败是成功之母，想失败，就多成功。",
        "菠萝biu~菠萝biu~",
        "恐龙抗狼抗狼抗",
        "最迷人的最危险",
        "星星之火，可以燎原",
        "大漠沙如雪，燕山月似钩。",
        "氢氢敲醒沉睡的心灵",
        "瘦巴巴的老爷们，一起走哇",
        "9（6翻了）",
        "发掘无限创意，开启编程之旅。",
        "不识庐山真面目，只缘身在此山中",
        "我命由我不由天",
        "记忆是痛苦的根源。",
        "野旷天低树，江清月近人",
        "世上无难事，只要肯放弃。",
        "我就是小气，想让你成为我一个人的专利",
        "人生中最大的遗憾，就是没和初恋在一起吧...",
        "欲买桂花同载酒，终不似、少年游。",
        "世界那么大，我想去看看",
        "原神，启动！",
        "海内存知己，天涯若比邻",
        "离离原上谱，越来越离谱",
        "学好数理化，走遍天下都不怕",
        "木叶飞舞之处，火亦生生不息",
        "欲买桂花同载酒，荒泷天下第一斗。",
        "三长一短选最短，三短一长选最长",
        "人是要整活的。因为不整活，不就死了吗？",
        "Nya~",
        "看着风景美景美如画，本想吟诗赠天下。奈何本君没文化，一句卧槽风好大。",
        "shift",
        "有志者事竟成",
        "啊巴啊巴啊巴",
        "风吹柳叶遮黄雀，薄翅不觉已落蝉。",
        "忽如一夜春风来，千树万树梨花开。",
        "任何邪恶，终将绳之以法",
        "妮可妮可妮~",
        "盼望着，盼望着，东风来了，春天的脚步近了。",
        "其实世界上没有路，走的人多了，变形成了路。",
        "与时间赛跑",
        "一年之计在于春",
        "一日之计在于晨",
        "你总是这样轻言放弃的话，无论多久都只会原地踏步",
        "天空是青红色，窗外有核辐射。",
        "趁着年轻，好好犯病。",
        "海上生明月，天涯共此时。",
        "没有人类的文明，毫无意义。",
        "让人类保持理智，确实是一种奢求。",
        "花有重开日，人无再少年。",
        "6",
        "即使听一万遍反方向的钟，你也不回来.",
        "尽管我拥有了全世界，也还是没法拥有你.",
        "只有失去了才懂得珍惜.",
        "珍惜眼前人，心存感恩。",
        "积极向上，无所畏惧。",
        "勇往直前，才能到达目标。",
        "善待他人，善待自己。",
        "热爱生活，享受每一天。",
        "山重水复疑无路，柳暗花明又一村。",
        "春江潮水连海平，海上明月共潮生。",
        "人间四月芳菲尽，山寺桃花始盛开。",
        "枯藤老树昏鸦，小桥流水人家。",
        "千山鸟飞绝，万径人踪灭。",
        "为什么太阳不结婚？因为太阳到处晒。",
        "为什么刘备顶着个大光头？因为他是个“无发”之人。",
        "有一只猫叫三条腿，它一跳就变成了二条腿。",
        "小明：妈妈，我的牙掉了！ 妈妈：放在牙床下面，明天会有一块元钱。 小明：那大人的呢？",
        "什么动物最喜欢读书？书虫。",
        "心事随风，无处安放。",
        "无助的孤单，一遍又一遍。",
        "失去了你，失去了整个世界。",
        "痛彻心扉，难以自拔。",
        "风吹散了我的梦，泪湿了我的夜。",
        "寂寞如影，无人能懂。",
        "心如刀割，痛不欲生。",
        "默默流淌的泪水，谁能懂得？",
        "时光老去，回忆阑珊。",
        "回首往事，泪水满满。",
        "心碎成千上万的碎片。",
        "孤独是最深的伤痛。",
        "失去爱的人，是多么的脆弱和孤单。",
        "回首过往，心如刀绞。",
        "伤感的心情，无法言喻。",
        "演绎着自己的悲伤，无人识别。",
        "那些过去的泪水，再也洗不净心灵。",
        "心如寒冬，冰冷无比。",
        "冷漠的世界，没有温暖可依靠。",
        "失去了你，心已被撕裂。",
        "无声的哭泣，淹没在黑暗中。",
        "冷漠的背影，让人心伤。",
        "无言的离别，痛彻心扉。",
        "心如断线的风筝，飘荡在空旷的天空。",
        "梦醒时分，泪已成河。",
        "刻骨铭心的伤害，犹如刀割。",
        "遗憾的悲伤，无法填补。",
        "孤独是心底最深的伤痛。",
        "无尽的寂寞，漫过心间。",
        "思念像一缕清风，轻轻拂过心间。",
        "心之所动，泪随所溢。",
        "遥望远方，离别如此滋味。",
        "浮生若梦，情深难舍。",
        "失去不是最痛苦的事，最痛苦的是爱过。",
        "冰冷的夜色里，心在微微颤抖。",
        "回忆是最美的刺痛，带来岁月的沉重。",
        "难过的日子里，寂寞如影相伴。",
        "心碎成一地的瓣瓣花，无人采撷。",
        "断了线的风筝，追不回失去的曾经。",
        "冷漠的眼神，让我心如刀割。",
        "纵然泪眼朦胧，也要坚强面对。",
        "世间万物，唯有孤独永恒。",
        "为什么鸟儿不会玩扑克牌？因为它会打鸟语。",
        "有一只蚂蚁站在午餐盒上大声喊：“帮帮我！有个巨大的怪物追着我！”, 旁边的蜘蛛回答：“算了吧，你说得太夸张了。你还没看见那只怪物吃我的时候是什么表情呢！”",
        "有一只乌龟在大雨中站了很久，终于等到阴晴不定的天气，它高兴地说：'哇，好凉快啊！'",
        "有一天，小明对爸爸说：“爸爸，我长大了，我想去外太空。”, 爸爸问：“你为什么要去外太空？”, 小明回答：“因为那里没有作业！”",
        "青山一道同云雨，明月何曾是两乡。",
        "采得百花成蜜后，为谁辛苦为谁甜。",
        "花开堪折直须折，莫待无花空折枝。",
        "山外青山楼外楼，西湖歌舞几时休。",
        "问余何意栖碧山，笑而不语心自闲。",
        "千年之前，悠然诗琴麻衫岭。",
        "春风又绿江南岸，明月何时照我还。",
        "采菊东篱下，悠然见南山。",
        "夕阳无限好，只是近黄昏。",
        "满地黄花堆积。憔悴损，如今有谁堪摘？",
        "两个黄鹂鸣翠柳，一行白鹭上青天。",
        "不畏浮云遮望眼，只缘身在最高层。",
        "东篱乌啼，一夜湘君百忧愁。",
        "白日依山尽，黄河入海流。",
        "黄河远上白云间，一片孤城万仞山。",
        "梅子黄时日日晴，小溪泛尽却山行。",
        "遥知不是雪，为有暗香来。",
        "碧云天，黄叶地，秋色连波，波上寒烟翠。",
        "小楼昨夜又东风，故国不堪回首月明中。",
        "天若有情天亦老，人间正道是沧桑。",
        "小明对小红说：“你们班上有个男生长得像章鱼。”, 小红问：“长得像章鱼？为什么？”, 小明回答：“因为他有八个妈妈！”",
        "有一只猴子站在树上看到远处有一只狮子向这边跑来，它大声说：“你走开！离我远点！”, 狮子继续向前跑来，猴子又大声说：“我再说一遍，你走开！离我远点！”, 狮子停下来，抬起脖子看着猴子说：“你以为我怕你吗？”, 猴子摇摇头说：“不是，我怕你喷口水。”",
        "小明：爸爸，你知道吗，我今天和一个小朋友打了架！, 爸爸：为什么？, 小明：他问我有啥本事，我说我可以闭上眼睛骑自行车，他就说那不算，然后我就打了他一巴掌。",
        "有一天，老师问小明：“小明，你的作业怎么没写？”, 小明回答：“老师，我忘了带家庭作业本。”, 老师说：“小明，你真是一个忘性大王！”, 小明冲出教室后喃喃自语：“忘了带作业本，还记得我是国王。”",
    ]

    random_quote = random.choice(quotes)
    
    data = {"quote": random_quote}
    return json.dumps(data)

if __name__ == "__main__":
    app.run(port=80, debug=True)