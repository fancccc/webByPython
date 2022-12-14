from PublicReference.base import *


class 主动技能(主动技能):
    def 等效CD(self, 武器类型, 输出类型):
        return round(self.CD / self.恢复, 1)


class 职业主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    data0 = []
    data1 = []
    data2 = []
    data3 = []

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if len(self.data0) >= self.等级 and len(self.data0) > 0:
            等效倍率 += self.data0[self.等级] * self.攻击次数
        if len(self.data1) >= self.等级 and len(self.data1) > 0:
            等效倍率 += self.data1[self.等级] * self.攻击次数2
        if len(self.data2) >= self.等级 and len(self.data2) > 0:
            等效倍率 += self.data2[self.等级] * self.攻击次数3
        if len(self.data3) >= self.等级 and len(self.data3) > 0:
            等效倍率 += self.data3[self.等级] * self.攻击次数4
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能0(职业主动技能):
    名称 = '崩拳'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    data0 = [int(i*1.0) for i in [0, 2766, 3046, 3327, 3608, 3888, 4169, 4450, 4730, 5011, 5292, 5572, 5853, 6134, 6414, 6695, 6975, 7256, 7537, 7817, 8098, 8379, 8659, 8940, 9221, 9501, 9782, 10063, 10343, 10624, 10904, 11185, 11466, 11746, 12027, 12308,
                                  12588, 12869, 13150, 13430, 13711, 13992, 14272, 14553, 14833, 15114, 15395, 15675, 15956, 16237, 16517, 16798, 17079, 17359, 17640, 17921, 18201, 18482, 18762, 19043, 19324, 19604, 19885, 20166, 20446, 20727, 21008, 21288, 21569, 21850, 22130]]
    CD = 6.0
    TP成长 = 0.1
    TP上限 = 5


class 技能1(职业主动技能):
    名称 = '铁山靠'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data0 = [int(i*1.0) for i in [0, 3973, 4376, 4779, 5182, 5585, 5988, 6391, 6794, 7197, 7600, 8003, 8407, 8810, 9213, 9616, 10019, 10422, 10825, 11228, 11631, 12034, 12437, 12840, 13243, 13647, 14050, 14453, 14856, 15259, 15662, 16065, 16468, 16871, 17274,
                                  17677, 18080, 18483, 18886, 19290, 19693, 20096, 20499, 20902, 21305, 21708, 22111, 22514, 22917, 23320, 23723, 24126, 24530, 24933, 25336, 25739, 26142, 26545, 26948, 27351, 27754, 28157, 28560, 28963, 29366, 29770, 30173, 30576, 30979, 31382, 31785]]
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.5


class 技能2(职业主动技能):
    名称 = '碎骨'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data0 = [int(i*1.0) for i in [0, 4067, 4480, 4892, 5305, 5718, 6130, 6543, 6956, 7368, 7781, 8194, 8606, 9019, 9432, 9844, 10257, 10670, 11082, 11495, 11908, 12320, 12733, 13146, 13558, 13971, 14383, 14796, 15209, 15621, 16034, 16447, 16859, 17272, 17685,
                                  18097, 18510, 18923, 19335, 19748, 20161, 20573, 20986, 21399, 21811, 22224, 22637, 23049, 23462, 23875, 24287, 24700, 25113, 25525, 25938, 26351, 26763, 27176, 27588, 28001, 28414, 28826, 29239, 29652, 30064, 30477, 30890, 31302, 31715, 32128, 32540]]
    CD = 7.0
    TP成长 = 0.1
    TP上限 = 5


class 技能3(被动技能):
    名称 = '柔化肌肉'
    所在等级 = 30
    等级上限 = 15
    基础等级 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.125 + 0.015 * self.等级, 5)


class 技能4(被动技能):
    名称 = '弱点感知'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 10:
                return round(1.01 + 0.01 * self.等级, 5)
            else:
                return round(1.11 + 0.02 * (self.等级-10), 5)


class 技能5(职业主动技能):
    名称 = '寸拳'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data0 = [int(i*1.0) for i in [0, 9074, 9994, 10915, 11836, 12756, 13677, 14597, 15518, 16438, 17359, 18280, 19200, 20121, 21041, 21962, 22883, 23803, 24724, 25644, 26565, 27485, 28406, 29327, 30247, 31168, 32088, 33009, 33930, 34850, 35771, 36691, 37612, 38532,
                                  39453, 40374, 41294, 42215, 43135, 44056, 44977, 45897, 46818, 47738, 48659, 49579, 50500, 51421, 52341, 53262, 54182, 55103, 56024, 56944, 57865, 58785, 59706, 60626, 61547, 62468, 63388, 64309, 65229, 66150, 67071, 67991, 68912, 69832, 70753, 71673, 72594]]
    CD = 15
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.5

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.24 + 0.09


class 技能6(职业主动技能):
    名称 = '升龙拳'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data0 = [int(i*1.0) for i in [0, 1961, 2160, 2359, 2558, 2757, 2956, 3155, 3354, 3553, 3752, 3951, 4150, 4349, 4548, 4747, 4946, 5145, 5343, 5542, 5741, 5940, 6139, 6338, 6537, 6736, 6935, 7134, 7333, 7532, 7731, 7930, 8129, 8328, 8527, 8726,
                                  8925, 9124, 9323, 9522, 9721, 9920, 10119, 10318, 10517, 10716, 10915, 11114, 11313, 11512, 11711, 11910, 12109, 12308, 12507, 12706, 12905, 13104, 13303, 13502, 13701, 13900, 14099, 14298, 14496, 14695, 14894, 15093, 15292, 15491, 15690]]
    攻击次数 = 4
    data1 = [int(i*1.0) for i in [0, 1699, 1871, 2043, 2216, 2388, 2561, 2733, 2905, 3078, 3250, 3422, 3595, 3767, 3940, 4112, 4284, 4457, 4629, 4802, 4974, 5146, 5319, 5491, 5663, 5836, 6008, 6181, 6353, 6525, 6698, 6870, 7042, 7215, 7387,
                                  7560, 7732, 7904, 8077, 8249, 8422, 8594, 8766, 8939, 9111, 9283, 9456, 9628, 9801, 9973, 10145, 10318, 10490, 10662, 10835, 11007, 11180, 11352, 11524, 11697, 11869, 12041, 12214, 12386, 12559, 12731, 12903, 13076, 13248, 13421, 13593]]
    攻击次数2 = 1
    # 倍率 =  1.073
    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 2.0


class 技能7(职业主动技能):
    名称 = '闪电之舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    data0 = [int(i*1.0) for i in [0, 2119, 2334, 2549, 2764, 2979, 3194, 3409, 3624, 3839, 4055, 4270, 4485, 4700, 4915, 5130, 5345, 5560, 5775, 5990, 6205, 6420, 6635, 6850, 7065, 7280, 7495, 7710, 7925, 8140, 8355, 8570, 8785, 9000, 9215, 9430,
                                  9646, 9861, 10076, 10291, 10506, 10721, 10936, 11151, 11366, 11581, 11796, 12011, 12226, 12441, 12656, 12871, 13086, 13301, 13516, 13731, 13946, 14161, 14376, 14591, 14806, 15021, 15237, 15452, 15667, 15882, 16097, 16312, 16527, 16742, 16957]]
    攻击次数 = 7
    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 1
    是否有护石 = 1
    演出时间 = 2.2

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 0.92
            self.攻击次数 += 2
            self.CD *= 0.85
            self.演出时间 = 2.7
        elif x == 1:
            self.倍率 *= 0.99
            self.攻击次数 += 2
            self.CD *= 0.85
            self.演出时间 = 2.7


class 技能8(职业主动技能):
    名称 = '纷影连环踢'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    data0 = [int(i*1.0) for i in [0, 586, 646, 705, 765, 824, 884, 943, 1003, 1062, 1122, 1181, 1241, 1300, 1360, 1419, 1479, 1538, 1598, 1657, 1717, 1776, 1836, 1895, 1955, 2014, 2074, 2133, 2193, 2252, 2312, 2371, 2431, 2490,
                                  2550, 2609, 2669, 2728, 2788, 2847, 2907, 2966, 3026, 3085, 3145, 3204, 3264, 3323, 3383, 3442, 3502, 3561, 3621, 3680, 3740, 3799, 3859, 3918, 3978, 4037, 4097, 4156, 4216, 4275, 4335, 4394, 4454, 4513, 4573, 4632, 4692]]
    攻击次数 = 10
    data1 = [int(i*1.0) for i in [0, 13012, 14333, 15653, 16973, 18293, 19613, 20933, 22253, 23574, 24894, 26214, 27534, 28854, 30174, 31494, 32815, 34135, 35455, 36775, 38095, 39415, 40735, 42056, 43376, 44696, 46016, 47336, 48656, 49977, 51297, 52617, 53937, 55257,
                                  56577, 57897, 59218, 60538, 61858, 63178, 64498, 65818, 67138, 68459, 69779, 71099, 72419, 73739, 75059, 76379, 77700, 79020, 80340, 81660, 82980, 84300, 85621, 86941, 88261, 89581, 90901, 92221, 93541, 94862, 96182, 97502, 98822, 100142, 101462, 102782, 104103]]
    攻击次数2 = 1
    CD = 40.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.演出时间 = 4.4
            self.倍率 *= 0.87
            self.攻击次数 = 20
        elif x == 1:
            self.演出时间 = 4.4
            self.倍率 *= 0.98
            self.攻击次数 = 20


class 技能9(职业主动技能):
    名称 = '武神强踢'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    data0 = [0, 48861, 60190, 71520, 82851, 94181, 105511, 116842, 128172, 139501, 150831, 162162, 173492, 184821, 196151, 207482, 218812, 230142, 241473, 252803, 264132, 275462, 286793, 298123, 309452, 320783, 332113, 343443, 354773, 366103, 377434, 388763, 400093, 411424, 422754, 434083,
             445414, 456744, 468074, 479404, 490734, 502065, 513394, 524725, 536054, 547385, 558714, 570045, 581375, 592705, 604035, 615365, 626696, 638025, 649356, 660685, 672016, 683345, 694676, 706006, 717336, 728667, 739996, 751327, 762656, 773987, 785316, 796647, 807977, 819307, 830636]
    CD = 145.0
    演出时间 = 0.5

    def 等效百分比(self, 武器类型):
        # 6级特效+10%强踢攻击力,目前没有体现在技能面板上
        if self.等级 >= 6:
            self.倍率 *= 1.1
        return super().等效百分比(武器类型)


class 技能10(被动技能):
    名称 = '武神步'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.05 + 0.02 * self.等级, 5)


class 技能11(职业主动技能):
    名称 = '破碎拳'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    #基础 = 18861.4546
    #成长 = 2129.5454
    data0 = [int(i*1.0) for i in [0, 20991, 23120, 25251, 27380, 29509, 31639, 33768, 35899, 38028, 40157, 42287, 44416, 46545, 48676, 50805, 52935, 55064, 57193, 59324, 61453, 63583, 65712, 67841, 69972,
                                  72101, 74231, 76360, 78489, 80620, 82749, 84879, 87008, 89137, 91267, 93397, 95527, 97656, 99785, 101915, 104045, 106174, 108304, 110433, 112563, 114693, 116822, 118952, 121081, 123211, 125341]]
    CD = 30
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.5

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.19 + 0.09


class 技能12(职业主动技能):
    名称 = '回天连环击'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    # 横扫地面攻击力：<data0>%
    data0 = [0, 2863, 3153, 3444, 3734, 4025, 4315, 4606, 4896, 5187, 5477, 5768, 6059, 6349, 6640, 6930, 7221, 7511, 7802, 8092, 8383, 8673, 8964, 9254, 9544, 9835, 10125,
             10416, 10706, 10997, 11287, 11578, 11868, 12159, 12450, 12740, 13031, 13321, 13612, 13902, 14193, 14483, 14774, 15064, 15354, 15645, 15935, 16226, 16516, 16807, 17097]
    攻击次数 = 1
    # 寸劲攻击力：<data1>%
    data1 = [0, 5939, 6541, 7144, 7747, 8349, 8951, 9554, 10157, 10759, 11362, 11964, 12567, 13169, 13772, 14375, 14977, 15579, 16182, 16785, 17387, 17990, 18592, 19195, 19797, 20400,
             21003, 21605, 22207, 22810, 23413, 24015, 24618, 25221, 25823, 26425, 27028, 27631, 28233, 28835, 29438, 30041, 30643, 31246, 31849, 32450, 33053, 33656, 34259, 34861, 35464]
    攻击次数2 = 1
    # 正拳攻击力：<data2>%
    data2 = [0, 8820, 9715, 10610, 11505, 12399, 13295, 14189, 15084, 15978, 16874, 17768, 18663, 19559, 20453, 21348, 22242, 23138, 24032, 24927, 25822, 26717, 27612, 28506, 29402,
             30296, 31191, 32086, 32981, 33876, 34770, 35665, 36560, 37455, 38350, 39244, 40140, 41034, 41929, 42824, 43719, 44614, 45508, 46404, 47298, 48193, 49087, 49983, 50877, 51772, 52668]
    攻击次数3 = 1
    # 环绕攻击力：<data3>%
    data3 = [0, 11571, 12745, 13920, 15094, 16268, 17441, 18615, 19789, 20963, 22137, 23311, 24485, 25659, 26833, 28007, 29181, 30355, 31529, 32703, 33877, 35050, 36224, 37399, 38573,
             39747, 40921, 42095, 43268, 44442, 45616, 46790, 47965, 49139, 50313, 51486, 52660, 53834, 55008, 56182, 57356, 58530, 59705, 60878, 62052, 63226, 64400, 65574, 66748, 67922, 69095]
    攻击次数4 = 1
    CD = 50
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 2.2

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.倍率 *= 1.34
        elif x == 1:
            self.攻击次数 = 0
            self.倍率 *= (1.34 + 0.08)


class 技能13(被动技能):
    名称 = '神武之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.22 + 0.02 * self.等级, 5)


class 技能14(职业主动技能):
    名称 = '虎啸神拳'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    #基础 = 1581.4
    #成长 =178.6
    data0 = [int(i*1.0) for i in [0, 1760, 1938, 2117, 2296, 2474, 2653, 2831, 3010, 3188, 3367, 3546, 3724, 3903, 4081, 4260, 4439, 4617, 4796, 4974, 5153, 5331, 5510, 5689, 5867, 6046, 6224, 6403, 6582, 6760, 6939, 7117, 7296, 7474, 7653,
                                  7832, 8010, 8189, 8367, 8546, 8725, 8903, 9082, 9260, 9439, 9617, 9796, 9975, 10153, 10332, 10510, 10689, 10868, 11046, 11225, 11403, 11582, 11760, 11939, 12118, 12296, 12475, 12653, 12832, 13011, 13189, 13368, 13546, 13725, 13903, 14082]]
    攻击次数 = 15
    #基础2 = 15453.2
    #成长2 =1744.8
    data1 = [int(i*1.0) for i in [0, 17198, 18943, 20688, 22433, 24177, 25922, 27667, 29412, 31157, 32901, 34646, 36391, 38136, 39881, 41626, 43370, 45115, 46860, 48605, 50350, 52094, 53839, 55584, 57329, 59074, 60818, 62563, 64308, 66053, 67798, 69542, 71287, 73032, 74777, 76522,
                                  78266, 80011, 81756, 83501, 85246, 86990, 88735, 90480, 92225, 93970, 95714, 97459, 99204, 100949, 102694, 104438, 106183, 107928, 109673, 111418, 113162, 114907, 116652, 118397, 120142, 121886, 123631, 125376, 127121, 128866, 130610, 132355, 134100, 135845, 137590]]
    攻击次数2 = 1
    # 基础3=4083.8667
    # 成长3=461.1333
    data2 = [int(i*1.0) for i in [0, 4545, 5006, 5467, 5928, 6390, 6851, 7312, 7773, 8234, 8695, 9156, 9618, 10079, 10540, 11001, 11462, 11923, 12384, 12845, 13307, 13768, 14229, 14690, 15151, 15612, 16073, 16535, 16996, 17457, 17918, 18379, 18840, 19301, 19763,
                                  20224, 20685, 21146, 21607, 22068, 22529, 22991, 23452, 23913, 24374, 24835, 25296, 25757, 26219, 26680, 27141, 27602, 28063, 28524, 28985, 29446, 29908, 30369, 30830, 31291, 31752, 32213, 32674, 33136, 33597, 34058, 34519, 34980, 35441, 35902, 36364]]
    攻击次数3 = 1
    CD = 40.0
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 2 * 0.83


class 技能15(职业主动技能):
    名称 = '无影脚'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    # 扫腿攻击力：<int>%
    data0 = [0, 5425, 5975, 6526, 7075, 7625, 8176, 8726, 9276, 9827, 10377, 10928, 11479, 12029, 12579, 13129, 13680, 14230, 14780, 15331, 15881, 16430, 16982, 17532, 18082, 18633, 19183, 19733, 20284, 20834, 21384, 21934, 22486, 23036, 23586, 24137,
             24687, 25236, 25787, 26337, 26887, 27438, 27989, 28539, 29090, 29640, 30190, 30740, 31291, 31841, 32391, 32942, 33493, 34043, 34593, 35143, 35693, 36244, 36794, 37344, 37895, 38445, 38995, 39545, 40097, 40647, 41197, 41748, 42298, 42848, 43399]
    攻击次数 = 1
    # 第2击物理攻击力：<data1>%
    data1 = [0, 2743, 3020, 3298, 3577, 3855, 4133, 4411, 4690, 4967, 5245, 5524, 5802, 6080, 6358, 6637, 6914, 7192, 7471, 7750, 8028, 8307, 8584, 8862, 9140, 9419, 9697, 9975, 10254, 10531, 10809, 11087, 11366, 11644, 11922, 12201, 12479,
             12757, 13035, 13314, 13592, 13870, 14148, 14426, 14704, 14982, 15261, 15539, 15817, 16095, 16373, 16651, 16929, 17209, 17487, 17764, 18043, 18321, 18599, 18878, 19156, 19434, 19711, 19990, 20268, 20546, 20825, 21103, 21381, 21658, 21938]
    攻击次数2 = 1
    # 第3击物理攻击力：<data2>%
    data2 = [0, 2745, 3024, 3303, 3581, 3859, 4138, 4417, 4695, 4975, 5253, 5531, 5809, 6088, 6367, 6645, 6924, 7202, 7481, 7760, 8038, 8316, 8595, 8874, 9152, 9432, 9710, 9987, 10267, 10545, 10824, 11103, 11381, 11659, 11937, 12217, 12495,
             12773, 13052, 13331, 13609, 13888, 14167, 14444, 14724, 15002, 15281, 15560, 15838, 16116, 16395, 16674, 16952, 17231, 17509, 17788, 18067, 18345, 18624, 18901, 19181, 19459, 19738, 20017, 20294, 20573, 20852, 21131, 21409, 21688, 21966]
    攻击次数3 = 1
    # 抽打物理攻击力：<int>%
    data3 = [0, 42893, 47244, 51595, 55947, 60299, 64650, 69002, 73353, 77704, 82055, 86407, 90758, 95109, 99462, 103813, 108164, 112516, 116868, 121218, 125570, 129922, 134273, 138625, 142977, 147327, 151679, 156031, 160382, 164733, 169086, 173437, 177788, 182139, 186491, 190842,
             195193, 199545, 203897, 208248, 212600, 216951, 221302, 225654, 230006, 234356, 238709, 243061, 247411, 251763, 256115, 260465, 264817, 269168, 273520, 277872, 282223, 286575, 290926, 295277, 299629, 303980, 308332, 312684, 317035, 321386, 325738, 330089, 334440, 338792, 343144]
    攻击次数4 = 1
    CD = 45.0
    是否有护石 = 1
    演出时间 = 2

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.攻击次数2 = 0
            self.攻击次数3 = 0
            self.攻击次数4 *= 1.66


class 技能16(职业主动技能):
    名称 = '极尽霸皇断空拳'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    #基础 =87153.5 *1.006068
    #成长 =26310.5 *1.006068
    # 断空拳物理攻击力：<data0>%
    data0 = [0, 114153, 140623, 167092, 193562, 220032, 246503, 272973, 299443, 325913, 352384, 378853, 405324, 431795, 458264, 484735, 511205, 537675, 564145, 590615, 617085, 643556, 670026, 696496, 722967, 749436, 775907, 802377, 828847, 855317, 881788, 908258, 934728, 961199, 987668, 1014139, 1040609,
             1067079, 1093548, 1120018, 1146489, 1172959, 1199429, 1225899, 1252370, 1278839, 1305310, 1331781, 1358250, 1384721, 1411191, 1437661, 1464131, 1490601, 1517071, 1543542, 1570012, 1596482, 1622953, 1649422, 1675893, 1702363, 1728833, 1755303, 1781774, 1808244, 1834714, 1861185, 1887654, 1914125, 1940595]
    CD = 180.0
    演出时间 = 1.2


class 技能17(被动技能):
    名称 = '疾风劲'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能18(职业主动技能):
    名称 = '雷霆之舞'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    # 第1~7击物理攻击力：<int>%
    data0 = [0, 10602, 11677, 12753, 13828, 14904, 15979, 17055, 18130, 19206, 20281, 21357, 22433, 23508, 24584, 25659, 26735, 27810, 28886, 29961,
             31037, 32112, 33188, 34263, 35339, 36414, 37490, 38566, 39641, 40717, 41792, 42868, 43943, 45019, 46094, 47170, 48245, 49321, 50396, 51472, 52547]
    攻击次数 = 7
    # 最后一击物理攻击力：<int>%
    data1 = [0, 31805, 35032, 38258, 41485, 44711, 47938, 51164, 54391, 57618, 60844, 64071, 67298, 70524, 73751, 76977, 80204, 83430, 86657, 89884, 93110, 96337,
             99563, 102790, 106017, 109243, 112470, 115697, 118923, 122150, 125376, 128603, 131829, 135056, 138283, 141509, 144736, 147962, 151189, 154416, 157642]
    攻击次数2 = 1
    CD = 60.0
    演出时间 = 6.2


class 技能19(职业主动技能):
    名称 = '真烈空星鸣拳'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']
    # 震脚冲击波物理攻击力：<int>%
    data0 = [0, 33740, 41564, 49388, 57212, 65035, 72859, 80683, 88507, 96331, 104154, 111978, 119802, 127626, 135450, 143273, 151097, 158921, 166745, 174569, 182392,
             190216, 198040, 205864, 213688, 221511, 229335, 237159, 244983, 252807, 260630, 268454, 276278, 284102, 291926, 299749, 307573, 315397, 323221, 331045, 338869]
    攻击次数 = 1
    # [武神强踢]物理攻击力：<int>%
    # [极尽 ： 霸皇断空拳]物理攻击力：<int>%
    data1 = [0, 67480, 83128, 98775, 114423, 130071, 145718, 161366, 177013, 192661, 208309, 223956, 239604, 255251, 270899, 286547, 302194, 317842, 333490, 349137, 364785,
             380432, 396080, 411728, 427375, 443023, 458670, 474318, 489966, 505613, 521261, 536908, 552556, 568204, 583851, 599499, 615146, 630794, 646442, 662089, 677737]
    攻击次数2 = 2
    # 烈空星鸣拳物理攻击力：<int>%
    data2 = [0, 118090, 145474, 172857, 200240, 227624, 255007, 282390, 309773, 337157, 364540, 391923, 419307, 446690, 474074, 501457, 528840, 556224, 583607, 610990, 638373,
             665757, 693140, 720523, 747907, 775290, 802673, 830057, 857440, 884823, 912206, 939590, 966973, 994356, 1021740, 1049123, 1076506, 1103890, 1131273, 1158656, 1186040]
    攻击次数3 = 1
    # 烈空星鸣拳多段物理攻击力：<int>% x 6
    data3 = [0, 8435, 10391, 12347, 14303, 16259, 18215, 20171, 22127, 24083, 26039, 27995, 29950, 31906, 33862, 35818, 37774, 39730, 41686, 43642,
             45598, 47554, 49510, 51466, 53422, 55378, 57334, 59290, 61246, 63202, 65158, 67114, 69070, 71025, 72981, 74937, 76893, 78849, 80805, 82761, 84717]
    攻击次数4 = 6
    # 基础 = 259160
    # 成长 = 78240
    CD = 290

    def 加成倍率(self, 武器类型):
        return 0
    演出时间 = 6.1

# CDR: 拳套精通(10%)
# 不包含觉醒


class 技能20(被动技能):
    名称 = '拳套精通'
    所在等级 = 15
    等级上限 = 10
    基础等级 = 10
    # 拳套精通cd
    关联技能 = ['无']
    冷却关联技能 = ['崩拳', '铁山靠', '碎骨', '寸拳', '升龙拳', '闪电之舞',
              '纷影连环踢', '破碎拳', '回天连环击', '虎啸神拳', '无影脚', '雷霆之舞']

    def 加成倍率(self, 武器类型):
        return 1.0

    def CD缩减倍率(self, 武器类型):
        if 武器类型 == '拳套':
            if self.等级 == 0:
                return 1.0
            else:
                return (1 - 0.01 * self.等级)
        else:
            return 1.0
    # 拳套自带全技能10cd
    冷却关联技能2 = ['所有']

    def CD缩减倍率2(self, 武器类型):
        if 武器类型 == '拳套':
            return 0.9
        elif 武器类型 == '臂铠':
            return 1.1
        else:
            return 1.0


# CDR 一觉cdr buff
class 技能21(被动技能):
    名称 = '武神强踢buff'
    所在等级 = 1
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['无']
    冷却关联技能 = ['所有']

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.9


技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能' + str(i) + '())')
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

归元·散打·女一觉序号 = 0
归元·散打·女二觉序号 = 0
归元·散打·女三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        归元·散打·女一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        归元·散打·女二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        归元·散打·女三觉序号 = 技能序号[i.名称]

归元·散打·女护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        归元·散打·女护石选项.append(i.名称)

归元·散打·女符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        归元·散打·女符文选项.append(i.名称)


class 归元·散打·女角色属性(角色属性):

    实际名称 = '归元·散打·女'
    角色 = '格斗家(女)'
    职业 = '散打'

    武器选项 = ['拳套', '臂铠']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 2.13

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def CD倍率计算(self):
        if "武神强踢" in self.技能栏[self.技能序号['真烈空星鸣拳']].关联技能:
            self.技能栏[self.技能序号['武神强踢buff']].等级 = 0
        super().CD倍率计算()


class 归元·散打·女(角色窗口):

    def 窗口属性输入(self):
        self.初始属性 = 归元·散打·女角色属性()
        self.角色属性A = 归元·散打·女角色属性()
        self.角色属性B = 归元·散打·女角色属性()
        self.一觉序号 = 归元·散打·女一觉序号
        self.二觉序号 = 归元·散打·女二觉序号
        self.三觉序号 = 归元·散打·女三觉序号
        self.护石选项 = deepcopy(归元·散打·女护石选项)
        self.符文选项 = deepcopy(归元·散打·女符文选项)
