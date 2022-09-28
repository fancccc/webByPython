from PublicReference.base import *


class 技能0(主动技能):
    名称 = '波动刻印'
    备注 = '(一轮,TP为基础精通)'
    所在等级 = 15
    等级上限 = 30
    基础等级 = 20
    基础 = 372
    CD = 1.0
    TP上限 = 3
    TP成长 = 0.1
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1.00 + 0.005 * self.等级, 5)
        else:
            return round(1.10 + 0.015 * (self.等级 - 20), 5)


class 技能1(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['波动刻印']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class 技能2(主动技能):
    名称 = '地裂·波动剑'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    #基础 = 1669.54
    #成长 = 188.48
    CD = 3.0
    TP成长 = 0.08
    TP上限 = 5
    数据 = [int(i*1.00) for i in [0, 1858, 2046, 2235, 2423, 2612, 2800, 2989, 3177, 3366, 3554, 3743, 3931, 4120, 4308, 4497, 4685, 4874, 5062, 5251, 5439, 5628, 5816, 6005, 6193, 6382, 6570, 6759, 6947, 7136, 7324, 7513, 7701, 7890, 8078, 8266, 8455, 8643, 8832, 9020, 9209, 9397, 9586, 9774, 9963, 10151, 10340, 10528, 10717, 10905, 11094, 11282, 11471, 11659, 11848, 12036, 12225, 12413, 12602, 12790, 12979, 13167, 13356, 13544, 13733, 13921, 14110, 14298, 14487, 14675, 14864]]
    攻击次数 = 1
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能3(主动技能):
    名称 = '鬼印珠'
    备注 = '(5印)'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    #基础 = 4485.24 * 1.003
    #成长 = 505.78 * 1.003
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5
    数据1 = [int(i*1.00) for i in [0, 111, 121, 133, 144, 156, 166, 178, 189, 201, 211, 223, 234, 246, 256, 268, 279, 291, 301, 313, 324, 335, 346, 358, 370, 380, 391, 403, 415, 425, 436, 448, 460, 470, 482, 493, 505, 515, 527, 538, 550, 560, 572, 583, 595, 605, 617, 628, 639, 650, 662, 673, 684, 695, 707, 718, 729, 740, 752, 763, 774, 785, 797, 809, 819, 830, 842, 854, 864, 876, 887]]
    攻击次数1 = 18
    数据2 = [int(i*1.00) for i in [0, 498, 550, 600, 650, 702, 752, 802, 854, 904, 954, 1006, 1056, 1106, 1157, 1208, 1258, 1309, 1360, 1410, 1461, 1512, 1562, 1613, 1663, 1714, 1765, 1815, 1866, 1917, 1967, 2018, 2069, 2119, 2169, 2221, 2271, 2321, 2373, 2423, 2473, 2525, 2575, 2625, 2677, 2727, 2777, 2829, 2879, 2929, 2981, 3031, 3081, 3132, 3183, 3233, 3284, 3335, 3385, 3436, 3487, 3537, 3588, 3638, 3689, 3740, 3790, 3841, 3892, 3942, 3993]]
    攻击次数2 = 1
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) *2* (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能4(主动技能):
    名称 = '邪光斩'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    #基础 = 5445.00
    #成长 = 615.10
    CD = 10.0
    TP成长 = 0.10
    TP上限 = 5
    数据 = [int(i*1.00) for i in [0, 2020, 2226, 2431, 2636, 2840, 3046, 3251, 3456, 3660, 3866, 4071, 4276, 4481, 4687, 4891, 5096, 5301, 5507, 5711, 5916, 6121, 6327, 6531, 6736, 6942, 7147, 7352, 7556, 7762, 7967, 8172, 8376, 8582, 8787, 8992, 9197, 9403, 9607, 9812, 10017, 10223, 10427, 10632, 10837, 11043, 11248, 11452, 11657, 11863, 12068, 12272, 12477, 12683, 12888, 13093, 13299, 13503, 13708, 13913, 14119, 14323, 14528, 14733, 14939, 15144, 15348, 15553, 15759, 15964, 16168]]
    攻击次数 = 3
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能5(被动技能):
    名称 = '修罗邪光斩'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['邪光斩']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.45 + 0.05 * self.等级, 5)


class 技能6(主动技能):
    名称 = '波动爆发'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 27
    #基础 = 4505.52
    #成长 = 854.50
    CD = 7.5
    TP成长 = 0.10
    TP上限 = 5
    数据 = [int(i*1.00) for i in [0, 5360, 6215, 7068, 7923, 8778, 9632, 10487, 11342, 12196, 13050, 13905, 14760, 15615, 16468, 17323, 18178, 19032, 19887, 20742, 21597, 22450, 23305, 24160, 25014, 25868, 26723, 27578, 28432, 29287, 30142, 30997, 31850, 32705, 33560, 34414, 35268, 36123, 36978, 37832, 38687, 39542, 40397, 41250, 42105, 42960, 43814, 44669, 45523, 46378, 47232, 48087, 48942, 49795, 50650, 51505, 52360, 53214, 54069, 54923, 55778, 56632, 57487, 58342, 59195, 60050, 60905, 61760, 62614, 63469, 64324]]
    攻击次数 = 1
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能7(被动技能):
    名称 = '挫折意志'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.13 + 0.02 * self.等级, 5)


class 技能8(主动技能):
    名称 = '冰刃·波动剑'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    #基础 = 4576.38 * 1.003
    #成长 = 517.63 * 1.003
    CD = 7
    TP成长 = 0.10
    TP上限 = 5
    数据 = [int(i*1.00) for i in [0, 566, 624, 681, 738, 795, 854, 912, 969, 1026, 1083, 1142, 1200, 1256, 1314, 1371, 1430, 1487, 1544, 1601, 1659, 1718, 1775, 1832, 1889, 1947, 2004, 2061, 2118, 2177, 2235, 2292, 2349, 2406, 2465, 2522, 2580, 2636, 2694, 2753, 2810, 2867, 2924, 2982, 3041, 3098, 3153, 3212, 3270, 3327, 3384, 3441, 3500, 3558, 3615, 3672, 3729, 3788, 3845, 3903, 3959, 4017, 4076, 4133, 4190, 4247, 4305, 4362, 4421, 4476, 4535]]
    攻击次数 = 9
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能9(主动技能):
    名称 = '杀意波动'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    #基础 = 570.95
    #成长 = 19.05
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 5
    数据 = [int(i*1.00) for i in [0, 295, 304, 314, 323, 333, 342, 352, 362, 371, 381, 390, 400, 409, 419, 428, 438, 448, 457, 467, 476]]
    攻击次数 = 2
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 等效CD(self, 武器类型, 输出类型):
        return 1


class 技能10(主动技能):
    名称 = '爆炎·波动剑'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    #基础 = 12157.50 * 0.993
    #成长 = 1371.18 * 0.993
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5
    数据1 = [int(i*1.00) for i in [0, 4473, 4926, 5381, 5835, 6288, 6740, 7196, 7649, 8103, 8556, 9009, 9464, 9917, 10371, 10824, 11279, 11733, 12186, 12641, 13094, 13548, 14001, 14456, 14910, 15363, 15818, 16271, 16725, 17177, 17633, 18084, 18539, 18992, 19446, 19899, 20354, 20808, 21261, 21716, 22169, 22623, 23076, 23531, 23984, 24438, 24893, 25346, 25800, 26253, 26706, 27161, 27614, 28070, 28521, 28974, 29429, 29882, 30336, 30791, 31244, 31698, 32151, 32606, 33059, 33513, 33968, 34421, 34875, 35328, 35783]]
    攻击次数1 = 3
    数据2 = [int(i*1.00) for i in [0, 10, 10, 11, 12, 13, 14, 15, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 66, 67, 68, 69, 70, 71, 72, 73]]
    攻击次数2 = 9
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能11(主动技能):
    名称 = '无双波'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    #基础 = 11427.86
    #成长 = 1290.17
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    数据 = [int(i*1.00) for i in [0, 6359, 7004, 7649, 8294, 8939, 9584, 10229, 10874, 11519, 12164, 12809, 13456, 14101, 14746, 15391, 16036, 16681, 17326, 17971, 18616, 19261, 19906, 20551, 21196, 21842, 22487, 23133, 23778, 24423, 25068, 25713, 26358, 27003, 27648, 28293, 28938, 29583, 30229, 30874, 31519, 32164, 32809, 33454, 34099, 34744, 35390, 36035, 36680, 37325, 37970, 38616, 39261, 39906, 40551, 41196, 41841, 42486, 43131, 43776, 44421, 45066, 45711, 46356, 47001, 47648, 48293, 48938, 49583, 50228, 50873]]
    攻击次数 = 2
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
        elif x == 1:
            self.倍率 *= 1.20 + 0.09


class 技能12(主动技能):
    名称 = '邪光波动阵'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    #基础 = 13024.19
    #成长 = 1470.99
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    数据1 = [int(i*1.00) for i in [0, 1450, 1597, 1744, 1891, 2038, 2185, 2332, 2479, 2626, 2774, 2921, 3068, 3215, 3362, 3509, 3656, 3803, 3950, 4098, 4245, 4392, 4539, 4686, 4833, 4980, 5127, 5274, 5422, 5569, 5716, 5863, 6010, 6157, 6304, 6451, 6598, 6746, 6893, 7040, 7187, 7334, 7481, 7628, 7775, 7922, 8070, 8217, 8364, 8511, 8658, 8805, 8952, 9099, 9246, 9394, 9541, 9688, 9835, 9982, 10129, 10276, 10423, 10570, 10718, 10865, 11012, 11159, 11306, 11453, 11600]]
    攻击次数1 = 1
    数据2 = [int(i*1.00) for i in [0, 1325, 1460, 1594, 1729, 1863, 1998, 2132, 2267, 2401, 2536, 2670, 2805, 2939, 3074, 3208, 3343, 3477, 3612, 3746, 3881, 4015, 4150, 4284, 4419, 4553, 4688, 4822, 4957, 5091, 5226, 5360, 5495, 5629, 5764, 5898, 6033, 6167, 6302, 6436, 6571, 6705, 6840, 6974, 7109, 7243, 7378, 7512, 7647, 7781, 7916, 8050, 8185, 8319, 8454, 8588, 8723, 8857, 8992, 9126, 9261, 9395, 9530, 9664, 9799, 9933, 10068, 10202, 10337, 10471, 10606]]
    攻击次数2 = 7
    数据3 = [int(i*1.00) for i in [0, 3770, 4152, 4535, 4917, 5300, 5682, 6065, 6447, 6830, 7212, 7595, 7977, 8360, 8742, 9125, 9507, 9890, 10272, 10654, 11037, 11419, 11802, 12184, 12567, 12949, 13332, 13714, 14097, 14479, 14862, 15244, 15627, 16009, 16392, 16774, 17157, 17539, 17922, 18304, 18687, 19069, 19452, 19834, 20217, 20599, 20982, 21364, 21747, 22129, 22512, 22894, 23277, 23659, 24042, 24424, 24806, 25189, 25571, 25954, 26336, 26719, 27101, 27484, 27866, 28249, 28631, 29014, 29396, 29779, 30161]]
    攻击次数3 = 1
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.15
            self.CD *= 0.85
        elif x == 1:
            self.倍率 *= 1.15 + 0.09
            self.CD *= 0.85


class 技能13(主动技能):
    名称 = '不动明王阵'
    备注 = '(5印)'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    #基础 = 26424.63 * 0.98
    #成长 = 2989.34 * 0.98
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    数据1 = [int(i*1.00) for i in [0, 321, 354, 386, 420, 452, 484, 518, 550, 582, 615, 648, 680, 713, 745, 778, 811, 843, 877, 909, 941, 975, 1007, 1039, 1072, 1105, 1137, 1170, 1203, 1236, 1268, 1300, 1334, 1366, 1398, 1432, 1464, 1496, 1530, 1562, 1594, 1627, 1660, 1693, 1725, 1757, 1791, 1823, 1855, 1889, 1921, 1953, 1987, 2019, 2051, 2084, 2117, 2150, 2182, 2215, 2248, 2280, 2312, 2346, 2378, 2410, 2444, 2476, 2509, 2542, 2574]]
    攻击次数1 = 30
    数据2 = [int(i*1.00) for i in [00, 4755, 5238, 5719, 6202, 6685, 7168, 7649, 8132, 8615, 9096, 9579, 10062, 10545, 11026, 11509, 11992, 12473, 12956, 13439, 13920, 14403, 14886, 15369, 15850, 16333, 16816, 17298, 17780, 18263, 18746, 19228, 19710, 20193, 20675, 21157, 21640, 22123, 22605, 23087, 23570, 24052, 24535, 25017, 25499, 25982, 26465, 26947, 27429, 27912, 28395, 28876, 29359, 29842, 30324, 30806, 31289, 31772, 32253, 32736, 33219, 33702, 34183, 34666, 35149, 35630, 36113, 36596, 37077, 37560, 38043]]
    攻击次数2 = 1
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) *2* (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2381
        elif x == 1:
            self.倍率 *= 1.31836


class 技能14(被动技能):
    名称 = '心眼'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['所有']
    关联技能2 = ['地裂·波动剑']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 16:
            return round(0.99 + 0.015 * self.等级, 5)
        else:
            return round(1.23 + 0.02 * (self.等级 - 16), 5)

    def 加成倍率2(self, 武器类型):
        return self.地波加成() / self.加成倍率(武器类型)

    def 地波加成(self):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 16:
            return round(1.105 + 0.015 * self.等级, 5)
        else:
            return round(1.345 + 0.02 * (self.等级 - 16), 5)


class 技能15(主动技能):
    名称 = '暗天波动眼'
    备注 = '(终结)'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    #基础 = 35457.01
    #成长 = 10704.25
    CD = 140.0
    数据 = [int(i*1.00) for i in [0, 46161, 56865, 67569, 78274, 88978, 99682, 110386, 121091, 131795, 142499, 153203, 163908, 174612, 185316, 196021, 206725, 217429, 228133, 238838, 249542, 260246, 270951, 281655, 292359, 303063, 313768, 324472, 335176, 345879, 356583, 367288, 377992, 388696, 399401, 410105, 420809, 431513, 442218, 452922, 463626, 474330, 485035, 495739, 506443, 517148, 527852, 538556, 549260, 559965, 570669, 581373, 592077, 602782, 613486, 624190, 634895, 645598, 656302, 667006, 677710, 688415, 699119, 709823, 720527, 731232, 741936, 752640, 763345, 774049, 784753]]
    攻击次数 = 1
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能16(主动技能):
    名称 = '波动剑·光翼'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    #基础 = 1907.14
    #成长 = 575.82
    TP成长 = 0.08
    CD = 1.2
    数据 = [int(i*1.00) for i in [0, 2482, 3059, 3635, 4210, 4786, 5362, 5938, 6513, 7089, 7666, 8241, 8817, 9392, 9969, 10545, 11120, 11696, 12272, 12848, 13423, 13999, 14576, 15151, 15727, 16302, 16879, 17455, 18030, 18606, 19182, 19758, 20333, 20909, 21486, 22061, 22637, 23212, 23789, 24365, 24940, 25516, 26092, 26668, 27244, 27820, 28396, 28971, 29547, 30124, 30699, 31275, 31850, 32427, 33002, 33578, 34154, 34730, 35306, 35881, 36457, 37034, 37609, 38185, 38760, 39337, 39913, 40488, 41064, 41640, 42216]]
    攻击次数 = 1
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能17(主动技能):
    名称 = '波动眼·天照'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    #基础 = 2301.63
    #成长 = 694.45
    TP成长 = 0.1
    CD = 2.5
    数据 = [int(i*1.00) for i in [0, 599, 738, 877, 1015, 1154, 1293, 1432, 1571, 1710, 1849, 1988, 2127, 2265, 2404, 2543, 2682, 2821, 2960, 3099, 3238, 3377, 3515, 3654, 3793, 3932, 4071, 4210, 4349, 4488, 4627, 4765, 4904, 5043, 5182, 5321, 5460, 5599, 5738, 5877, 6016, 6154, 6293, 6432, 6571, 6710, 6850, 6989, 7128, 7267, 7404, 7543, 7683, 7822, 7961, 8100, 8239, 8378, 8517, 8655, 8794, 8933, 9072, 9211, 9350, 9489, 9628, 9767, 9905, 10044, 10183]]
    攻击次数 = 5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能18(主动技能):
    名称 = '波动剑·闪枪'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    #基础 = 3975.32
    #成长 = 1199.99
    TP成长 = 0.1
    CD = 4.9
    数据 = [int(i*1.00) for i in [0, 739, 910, 1082, 1253, 1424, 1597, 1768, 1939, 2110, 2281, 2453, 2625, 2796, 2968, 3139, 3310, 3481, 3654, 3825, 3996, 4168, 4339, 4510, 4683, 4854, 5025, 5196, 5368, 5539, 5711, 5883, 6054, 6225, 6396, 6568, 6740, 6911, 7083, 7254, 7425, 7596, 7769, 7940, 8111, 8282, 8454, 8625, 8797, 8969, 9140, 9311, 9482, 9655, 9826, 9997, 10169, 10340, 10511, 10684, 10855, 11026, 11197, 11369, 11540, 11712, 11884, 12055, 12226, 12397, 12569]]
    攻击次数 = 7
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能19(主动技能):
    名称 = '波动剑·刺轮'
    备注 = '(含一轮平X)'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    #基础 = 4496.63
    #成长 = 1363.80
    CD = 1.0
    数据1 = [int(i*1.00) for i in [0, 940, 1159, 1376, 1595, 1813, 2030, 2249, 2467, 2686, 2903, 3122, 3340, 3557, 3776, 3994, 4213, 4430, 4649, 4867, 5086, 5303, 5521, 5740, 5957, 6176, 6394, 6613, 6830, 7048, 7267, 7484, 7703, 7921, 8140, 8357, 8576, 8794, 9011, 9230, 9448, 9667, 9884, 10103, 10321, 10539, 10757, 10975, 11194, 11411, 11630, 11848, 12066, 12284, 12502, 12721, 12938, 13157, 13375, 13593, 13811, 14030, 14247, 14465, 14684, 14902, 15120, 15338, 15557, 15774, 15992]]
    攻击次数1 = 1
    数据2 = [int(i*1.00) for i in [0, 1058, 1303, 1549, 1793, 2039, 2285, 2530, 2776, 3020, 3266, 3512, 3757, 4003, 4249, 4493, 4739, 4984, 5230, 5476, 5720, 5966, 6212, 6457, 6703, 6947, 7193, 7439, 7684, 7930, 8174, 8420, 8666, 8911, 9157, 9403, 9647, 9893, 10138, 10384, 10630, 10874, 11120, 11366, 11611, 11857, 12101, 12347, 12593, 12838, 13084, 13328, 13574, 13820, 14065, 14311, 14556, 14801, 15047, 15292, 15538, 15783, 16028, 16274, 16520, 16765, 17010, 17255, 17501, 17747, 17992]]
    攻击次数2 = 1
    数据3 = [int(i*1.00) for i in [0, 1175, 1448, 1720, 1993, 2266, 2539, 2812, 3084, 3357, 3629, 3902, 4175, 4447, 4720, 4993, 5266, 5539, 5810, 6083, 6356, 6629, 6902, 7174, 7447, 7720, 7993, 8266, 8537, 8810, 9083, 9356, 9629, 9901, 10174, 10447, 10720, 10993, 11264, 11537, 11810, 12083, 12356, 12628, 12901, 13174, 13447, 13720, 13991, 14264, 14537, 14810, 15083, 15355, 15628, 15901, 16174, 16447, 16718, 16991, 17264, 17537, 17810, 18082, 18355, 18628, 18901, 19173, 19445, 19718, 19991]]
    攻击次数3 = 1
    数据4 = [int(i*1.00) for i in [0, 270, 332, 395, 458, 520, 583, 646, 709, 771, 834, 897, 959, 1022, 1085, 1148, 1210, 1273, 1336, 1398, 1461, 1524, 1587, 1649, 1712, 1775, 1837, 1900, 1963, 2027, 2088, 2151, 2215, 2276, 2339, 2402, 2466, 2527, 2590, 2654, 2715, 2778, 2842, 2905, 2966, 3029, 3093, 3154, 3217, 3281, 3344, 3405, 3469, 3532, 3593, 3657, 3720, 3783, 3844, 3908, 3971, 4032, 4096, 4159, 4222, 4284, 4347, 4410, 4471, 4535, 4598]]
    攻击次数4 = 10
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3 + self.数据4[self.等级] * self.攻击次数4) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 等效CD(self, 武器类型, 输出类型):
        return 1


class 技能20(主动技能):
    名称 = '极冰·裂波剑'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    #基础 = 17180.21
    #成长 = 1939.91
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    数据1 = [int(i*1.00) for i in [0, 1835, 2021, 2208, 2393, 2580, 2766, 2954, 3138, 3324, 3512, 3696, 3884, 4070, 4254, 4442, 4628, 4815, 5000, 5187, 5373, 5558, 5745, 5931, 6119, 6303, 6491, 6677, 6861, 7049, 7235, 7422, 7607, 7794, 7980, 8166, 8352, 8538, 8726, 8912, 9096, 9284, 9470, 9657, 9842, 10029, 10215, 10400, 10587, 10773, 10961]]
    攻击次数1 = 3
    数据2 = [int(i*1.00) for i in [0, 2723, 2999, 3276, 3552, 3828, 4104, 4380, 4656, 4935, 5211, 5487, 5763, 6039, 6315, 6591, 6867, 7143, 7421, 7697, 7973, 8249, 8526, 8802, 9080, 9356, 9632, 9908, 10184, 10460, 10736, 11012, 11288, 11565, 11843, 12119, 12395, 12671, 12947, 13224, 13500, 13776, 14052, 14328, 14604, 14880, 15156, 15435, 15711, 15987, 16263]]
    攻击次数2 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2309
        elif x == 1:
            self.倍率 *= 1.32349


class 技能21(主动技能):
    名称 = '极炎·裂波剑'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    #基础 = 23087.13 * 1.009
    #成长 = 2606.72 * 1.009
    CD = 35.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    数据1 = [int(i*1.00) for i in [0, 4900, 5397, 5894, 6392, 6889, 7386, 7883, 8380, 8877, 9376, 9873, 10370, 10867, 11363, 11860, 12359, 12856, 13353, 13850, 14347, 14844, 15342, 15839, 16336, 16833, 17330, 17827, 18325, 18822, 19319, 19816, 20313, 20810, 21308, 21805, 22302, 22799, 23296, 23793, 24291, 24788, 25285, 25782, 26279, 26776, 27274, 27771, 28268, 28765, 29262]]
    攻击次数1 = 1
    数据2 = [int(i*1.00) for i in [0, 9802, 10796, 11790, 12785, 13779, 14773, 15768, 16762, 17756, 18751, 19745, 20739, 21734, 22728, 23722, 24717, 25711, 26705, 27701, 28695, 29688, 30684, 31678, 32672, 33667, 34661, 35655, 36650, 37644, 38638, 39633, 40627, 41621, 42616, 43610, 44604, 45599, 46593, 47587, 48583, 49576, 50570, 51566, 52560, 53554, 54549, 55543, 56537, 57532, 58526]]
    攻击次数2 = 1
    数据3 = [int(i*1.00) for i in [0, 748, 824, 900, 976, 1052, 1128, 1204, 1280, 1356, 1432, 1508, 1584, 1660, 1736, 1812, 1887, 1963, 2039, 2115, 2191, 2267, 2343, 2419, 2495, 2571, 2647, 2723, 2799, 2875, 2951, 3027, 3103, 3179, 3255, 3331, 3407, 3483, 3559, 3635, 3711, 3787, 3863, 3938, 4014, 4090, 4166, 4242, 4318, 4394, 4470]]
    攻击次数3 = 14
    数据4 = [int(i*1.00) for i in [0, 52, 56, 62, 66, 72, 78, 82, 88, 92, 98, 104, 108, 114, 120, 124, 130, 134, 140, 146, 150, 156, 160, 166, 172, 176, 182, 186, 192, 198, 202, 208, 212, 218, 224, 228, 234, 238, 244, 250, 254, 260, 264, 270, 276, 280, 286, 290, 296, 302, 306]]
    攻击次数4 = 13
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3 + self.数据4[self.等级] * self.攻击次数4) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2088
        elif x == 1:
            self.倍率 *= 1.29046


class 技能22(主动技能):
    名称 = '天雷·波动剑'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    #基础 = 65775.64
    #成长 = 7428.35
    CD = 40.0
    是否有护石 = 1
    数据1 = [int(i*1.00) for i in [0, 5261, 5795, 6328, 6862, 7397, 7930, 8464, 8997, 9531, 10066, 10599, 11133, 11666, 12200, 12735, 13268, 13802, 14335, 14869, 15404, 15937, 16471, 17004, 17538, 18073, 18606, 19140, 19673, 20207, 20742, 21275, 21809, 22342, 22876, 23411, 23944, 24478, 25011, 25545, 26080, 26613, 27147, 27681, 28214, 28749, 29282, 29816, 30350, 30883, 31418, 31951, 32485, 33019, 33552, 34087, 34620, 35154, 35688, 36221, 36756, 37289, 37823, 38357, 38890, 39425, 39958, 40492, 41026, 41559, 42094]]
    攻击次数1 = 11
    数据2 = [int(i*1.00) for i in [0, 14469, 15937, 17404, 18873, 20341, 21809, 23277, 24744, 26212, 27681, 29149, 30617, 32085, 33552, 35020, 36488, 37957, 39425, 40892, 42360, 43828, 45296, 46763, 48232, 49700, 51168, 52636, 54103, 55571, 57040, 58508, 59976, 61443, 62911, 64379, 65847, 67316, 68783, 70251, 71719, 73187, 74654, 76123, 77591, 79059, 80527, 81994, 83462, 84930, 86399, 87867, 89334, 90802, 92270, 93738, 95205, 96675, 98142, 99610, 101078, 102546, 104013, 105482, 106950, 108418, 109886, 111353, 112821, 114289, 115758]]
    攻击次数2 = 1
    数据3 = [int(i*1.00) for i in [0, 72, 80, 87, 94, 102, 109, 116, 124, 131, 138, 146, 153, 160, 168, 175, 182, 190, 197, 204, 212, 219, 226, 234, 241, 249, 256, 263, 271, 278, 285, 293, 300, 307, 315, 322, 329, 337, 344, 351, 359, 366, 373, 381, 388, 395, 403, 410, 417, 425, 432, 439, 447, 454, 461, 469, 476, 483, 491, 498, 505, 513, 520, 527, 535, 542, 549, 557, 564, 571, 579]]
    攻击次数3 = 12
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24


class 技能23(主动技能):
    名称 = '雷神之息'
    备注 = '(1次)'
    是否主动 = 0
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    #基础 = 3302.59
    #成长 = 624.43
    CD = 2.5
    关联技能 = ['所有']
    数据1 = [int(i*1.00) for i in [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 12, 12, 13, 14, 14, 15, 15, 16, 17, 17, 18, 19, 19, 20, 21, 21, 22, 22, 23, 24, 24, 25, 26, 26, 27, 28, 28, 29, 29, 30, 31, 31, 32, 33, 33, 34, 35, 35]]
    攻击次数1 = 1
    数据2 = [int(i*1.00) for i in [0, 3917, 4541, 5165, 5790, 6414, 7039, 7663, 8288, 8912, 9537, 10161, 10785, 11410, 12034, 12659, 13283, 13908, 14532, 15156, 15781, 16405, 17030, 17654, 18279, 18903, 19528, 20152, 20776, 21401, 22025, 22648, 23273, 23897, 24522, 25146, 25771, 26395, 27019, 27644, 28268, 28893, 29517, 30142, 30766, 31391, 32015, 32639, 33264, 33888, 34513]]
    攻击次数2 = 1
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 等效CD(self, 武器类型, 输出类型):
        return 2.5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.06 + 0.02 * self.等级, 5)


class 技能24(主动技能):
    名称 = '天雷·降魔杵'
    备注 = '(终结)'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    #基础 = 51915.63 * 0.999
    #成长 = 5865.91 * 0.999
    攻击次数 = 1
    CD = 45.0
    是否有护石 = 1
    数据1 = [int(i*1.00) for i in [0, 887, 978, 1068, 1159, 1248, 1339, 1428, 1519, 1608, 1698, 1789, 1879, 1968, 2058, 2149, 2239, 2329, 2418, 2509, 2599, 2689, 2779, 2870, 2960, 3050, 3140, 3231, 3321, 3410, 3500, 3591, 3681, 3770, 3861, 3950, 4041, 4131, 4221, 4310, 4401, 4491, 4582, 4671, 4762, 4852, 4942, 5031, 5122, 5212, 5302, 5392, 5482, 5572, 5662, 5752, 5842, 5933, 6023, 6113, 6204, 6294, 6384, 6473, 6563, 6654, 6744, 6833, 6923, 7014, 7104]]
    攻击次数1 = 26
    数据2 = [int(i*1.00) for i in [0, 8885, 9786, 10688, 11589, 12489, 13392, 14294, 15195, 16095, 16997, 17900, 18801, 19703, 20603, 21504, 22407, 23309, 24209, 25110, 26012, 26915, 27815, 28716, 29618, 30519, 31419, 32322, 33224, 34125, 35025, 35927, 36830, 37731, 38631, 39533, 40434, 41337, 42239, 43139, 44040, 44942, 45845, 46745, 47646, 48548, 49449, 50349, 51252, 52154, 53055, 53955, 54857, 55760, 56661, 57561, 58463, 59364, 60267, 61167, 62069, 62970, 63872, 64775, 65675, 66576, 67478, 68381, 69279, 70182, 71084]]
    攻击次数2 = 1
    数据3 = [int(i*1.00) for i in [0, 24846, 27366, 29886, 32409, 34929, 37449, 39969, 42492, 45012, 47532, 50052, 52572, 55095, 57615, 60135, 62655, 65177, 67698, 70218, 72738, 75260, 77780, 80301, 82821, 85343, 87863, 90383, 92904, 95426, 97946, 100466, 102986, 105509, 108029, 110549, 113069, 115589, 118112, 120632, 123152, 125672, 128193, 130715, 133235, 135756, 138276, 140796, 143318, 145839, 148359, 150879, 153399, 155922, 158442, 160962, 163482, 166005, 168525, 171045, 173565, 176085, 178608, 181128, 183648, 186168, 188690, 191211, 193731, 196251, 198773]]
    攻击次数3 = 1
    数据4 = [int(i*1.00) for i in [0, 38, 42, 46, 49, 53, 57, 61, 65, 69, 72, 76, 80, 84, 88, 92, 96, 99, 103, 107, 111, 115, 119, 122, 126, 130, 134, 138, 142, 145, 149, 153, 157, 161, 165, 169, 172, 176, 180, 184, 188, 192, 195, 199, 203, 207, 211, 215, 218, 222, 226, 230, 234, 238, 242, 245, 249, 253, 257, 261, 265, 268, 272, 276, 280, 284, 288, 291, 295, 299, 303]]
    攻击次数4 = 28
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3 + self.数据4[self.等级] * self.攻击次数4) * (1 + self.TP成长 * self.TP等级) * self.倍率

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35628


class 技能25(主动技能):
    名称 = '天雷·降魔杵(雷针)'
    备注 = '(1轮)'
    所在等级 = 80
    等级上限 = 1
    基础等级 = 1
    #基础 = 4952.01
    #成长 = 560.13
    CD = 2.5
    数据1 = [int(i*1.00) for i in [0, 887, 978, 1068, 1159, 1248, 1339, 1428, 1519, 1608, 1698, 1789, 1879, 1968, 2058, 2149, 2239, 2329, 2418, 2509, 2599, 2689, 2779, 2870, 2960, 3050, 3140, 3231, 3321, 3410, 3500, 3591, 3681, 3770, 3861, 3950, 4041, 4131, 4221, 4310, 4401, 4491, 4582, 4671, 4762, 4852, 4942, 5031, 5122, 5212, 5302, 5392, 5482, 5572, 5662, 5752, 5842, 5933, 6023, 6113, 6204, 6294, 6384, 6473, 6563, 6654, 6744, 6833, 6923, 7014, 7104]]
    攻击次数1 = 6
    数据2 = [int(i*1.00) for i in [0, 38, 42, 46, 49, 53, 57, 61, 65, 69, 72, 76, 80, 84, 88, 92, 96, 99, 103, 107, 111, 115, 119, 122, 126, 130, 134, 138, 142, 145, 149, 153, 157, 161, 165, 169, 172, 176, 180, 184, 188, 192, 195, 199, 203, 207, 211, 215, 218, 222, 226, 230, 234, 238, 242, 245, 249, 253, 257, 261, 265, 268, 272, 276, 280, 284, 288, 291, 295, 299, 303]]
    攻击次数2 = 6
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 等效CD(self, 武器类型, 输出类型):
        return 2.5


class 技能26(主动技能):
    名称 = '雷神降世：裁决'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    #基础 = 115355.09 * 0.996
    #成长 = 34839.29 * 0.996
    CD = 180
    数据1 = [int(i*1.00) for i in [0, 8853, 10908, 12960, 15014, 17067, 19119, 21173, 23228, 25280, 27333, 29387, 31439, 33494, 35547, 37599, 39653, 41706, 43758, 45813, 47867, 49919, 51972, 54026, 56078, 58133, 60186, 62238, 64292, 66344, 68397, 70452, 72506, 74558, 76611, 78663, 80718, 82772, 84825, 86877, 88931, 90983, 93038, 95091, 97145, 99197, 101250, 103302, 105357, 107411, 109464]]
    攻击次数1 = 1
    数据2 = [int(i*1.00) for i in [0, 2303, 2835, 3368, 3903, 4436, 4971, 5504, 6039, 6572, 7106, 7640, 8174, 8708, 9242, 9776, 10310, 10842, 11378, 11910, 12446, 12978, 13514, 14046, 14579, 15114, 15647, 16182, 16715, 17249, 17783, 18317, 18851, 19385, 19919, 20453, 20985, 21521, 22053, 22589, 23121, 23657, 24189, 24722, 25257, 25790, 26325, 26858, 27393, 27926, 28460]]
    攻击次数2 = 25
    数据3 = [int(i*1.00) for i in [0, 17708, 21816, 25922, 30027, 34136, 38241, 42347, 46455, 50561, 54668, 58773, 62880, 66987, 71093, 75200, 79307, 83412, 87519, 91626, 95732, 99839, 103946, 108051, 112158, 116265, 120371, 124478, 128585, 132690, 136796, 140904, 145010, 149118, 153224, 157329, 161438, 165543, 169649, 173757, 177863, 181968, 186077, 190182, 194288, 198396, 202502, 206607, 210716, 214821, 218927]]
    攻击次数3 = 1
    数据4 = [int(i*1.00) for i in [0, 63458, 78173, 92888, 107601, 122318, 137033, 151748, 166463, 181179, 195893, 210606, 225323, 240038, 254753, 269468, 284181, 298898, 313613, 328328, 343043, 357759, 372473, 387186, 401903, 416618, 431333, 446048, 460761, 475478, 490193, 504908, 519623, 534336, 549053, 563766, 578483, 593198, 607913, 622628, 637341, 652058, 666773, 681488, 696203, 710916, 725633, 740346, 755063, 769778, 784493]]
    攻击次数4 = 1
    数据5 = [int(i*1.00) for i in [0, 98, 121, 144, 167, 190, 212, 235, 258, 281, 304, 327, 349, 372, 395, 418, 441, 463, 486, 509, 532, 555, 577, 600, 623, 646, 669, 692, 714, 737, 760, 783, 806, 828, 851, 874, 897, 920, 942, 965, 988, 1011, 1034, 1057, 1079, 1102, 1125, 1148, 1171, 1193, 1216]]
    攻击次数5 = 28
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3 + self.数据4[self.等级] * self.攻击次数4+ self.数据5[self.等级] * self.攻击次数5) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能27(被动技能):
    名称 = '波动视界：慧眼'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能28(主动技能):
    名称 = '波动慧眼：无为法'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    #基础 = 121042.84
    #成长 = 13667.14
    CD = 60.0
    数据1 = [int(i*1.00) for i in [0, 6735, 7419, 8102, 8785, 9469, 10152, 10835, 11519, 12202, 12885, 13569, 14252, 14935, 15619, 16302, 16985, 17669, 18352, 19035, 19719, 20402, 21085, 21769, 22452, 23135, 23819, 24502, 25185, 25869, 26552, 27235, 27919, 28602, 29285, 29969, 30652, 31335, 32019, 32702, 33385]]
    攻击次数1 = 5
    数据2 = [int(i*1.00) for i in [0, 101035, 111286, 121536, 131786, 142036, 152286, 162536, 172786, 183036, 193286, 203536, 213786, 224036, 234286, 244536, 254786, 265036, 275286, 285536, 295786, 306036, 316286, 326536, 336786, 347036, 357286, 367536, 377786, 388036, 398286, 408536, 418786, 429036, 439286, 449536, 459786, 470036, 480286, 490537, 500787]]
    攻击次数2 = 1
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能29(主动技能):
    名称 = '波动神诀：万空'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    #基础 = 359630.24
    #成长 = 108568.10
    CD = 290
    关联技能 = ['无']
    数据1 = [int(i*1.00) for i in [0, 116714, 143778, 170842, 197906, 224970, 252035, 279099, 306163, 333227, 360291, 387355, 414420, 441484, 468548, 495612, 522676, 549740, 576805, 603869, 630933, 657997, 685061, 712125, 739190, 766254, 793318, 820382, 847446, 874511, 901575, 928639, 955703, 982767, 1009831, 1036896, 1063960, 1091024, 1118088, 1145152, 1172216, 1199281, 1226345, 1253409, 1280473, 1307537, 1334601, 1361666, 1388730, 1415794, 1442858, 1469922, 1496986, 1524051, 1551115, 1578179, 1605243, 1632307, 1659371, 1686436, 1713500, 1740564, 1767628, 1794692, 1821756, 1848821, 1875885, 1902949, 1930013, 1957077, 1984141]]
    攻击次数1 = 1
    数据2 = [int(i*1.00) for i in [0, 19452, 23963, 28473, 32984, 37495, 42005, 46516, 51027, 55537, 60048, 64559, 69070, 73580, 78091, 82602, 87112, 91623, 96134, 100644, 105155, 109666, 114176, 118687, 123198, 127709, 132219, 136730, 141241, 145751, 150262, 154773, 159283, 163794, 168305, 172816, 177326, 181837, 186348, 190858, 195369, 199880, 204390, 208901, 213412, 217922, 222433, 226944, 231455, 235965, 240476, 244987, 249497, 254008, 258519, 263029, 267540, 272051, 276561, 281072, 285583, 290094, 294604, 299115, 303626, 308136, 312647, 317158, 321668, 326179, 330690]]
    攻击次数2 = 6
    数据3 = [int(i*1.00) for i in [0, 58357, 71889, 85421, 98953, 112485, 126017, 139549, 153081, 166613, 180145, 193677, 207210, 220742, 234274, 247806, 261338, 274870, 288402, 301934, 315466, 328998, 342530, 356062, 369595, 383127, 396659, 410191, 423723, 437255, 450787, 464319, 477851, 491383, 504915, 518448, 531980, 545512, 559044, 572576, 586108, 599640, 613172, 626704, 640236, 653768, 667300, 680833, 694365, 707897, 721429, 734961, 748493, 762025, 775557, 789089, 802621, 816153, 829685, 843218, 856750, 870282, 883814, 897346, 910878, 924410, 937942, 951474, 965006, 978538, 992070]]
    攻击次数3 = 2
    数据4 = [int(i*1.00) for i in [0, 118058, 145434, 172810, 200186, 227562, 254938, 282314, 309690, 337066, 364442, 391818, 419194, 446570, 473946, 501322, 528698, 556074, 583450, 610826, 638202, 665578, 692954, 720330, 747706, 775082, 802458, 829834, 857210, 884586, 911962, 939338, 966714, 994090, 1021466, 1048842, 1076218, 1103594, 1130970, 1158346, 1185722, 1213098, 1240474, 1267850, 1295226, 1322602, 1349978, 1377354, 1404730, 1432106, 1459482, 1486858, 1514234, 1541610, 1568986, 1596362, 1623738, 1651114, 1678490, 1705866, 1733242, 1760618, 1787994, 1815370, 1842746, 1870122, 1897498, 1924874, 1952250, 1979626, 2007002]]
    攻击次数4 = 1
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3 + self.数据4[self.等级] * self.攻击次数4) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 加成倍率(self, 武器类型):
        return 0.0


技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能'+str(i)+'())')
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

极诣·阿修罗一觉序号 = 15
极诣·阿修罗二觉序号 = 26
极诣·阿修罗三觉序号 = 29


极诣·阿修罗护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        极诣·阿修罗护石选项.append(i.名称)

极诣·阿修罗符文选项 = ['无', '邪光斩', '波动爆发', '冰刃·波动剑', '鬼印珠', '爆炎·波动剑',
              '无双波', '邪光波动阵', '不动明王阵', '极冰·裂波剑', '极炎·裂波剑', '天雷·波动剑', '天雷·降魔杵']


class 极诣·阿修罗角色属性(角色属性):

    实际名称 = '极诣·阿修罗'
    角色 = '鬼剑士(男)'
    职业 = '阿修罗'

    武器选项 = ['太刀', '钝器', '巨剑', '短剑']

    类型选择 = ['魔法固伤']

    类型 = '魔法固伤'
    防具类型 = '板甲'
    防具精通属性 = ['智力']

    主BUFF = 1.59

    远古记忆 = 0
    刀魂之卡赞 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 伤害指数计算(self):

        self.技能栏[self.技能序号['波动剑·光翼']].等级 = self.技能栏[self.技能序号['暗天波动眼']].等级
        self.技能栏[self.技能序号['波动眼·天照']].等级 = self.技能栏[self.技能序号['暗天波动眼']].等级
        self.技能栏[self.技能序号['波动剑·闪枪']].等级 = self.技能栏[self.技能序号['暗天波动眼']].等级
        self.技能栏[self.技能序号['波动剑·刺轮']].等级 = self.技能栏[self.技能序号['暗天波动眼']].等级

        self.技能栏[self.技能序号['波动剑·光翼']].TP等级 = self.技能栏[self.技能序号['地裂·波动剑']].TP等级
        self.技能栏[self.技能序号['波动眼·天照']].TP等级 = self.技能栏[self.技能序号['冰刃·波动剑']].TP等级
        self.技能栏[self.技能序号['波动剑·闪枪']].TP等级 = self.技能栏[self.技能序号['爆炎·波动剑']].TP等级

        self.技能栏[self.技能序号['天雷·降魔杵(雷针)']].等级 = self.技能栏[self.技能序号['天雷·降魔杵']].等级
        self.技能栏[self.技能序号['天雷·降魔杵(雷针)']].倍率 = self.技能栏[self.技能序号['天雷·降魔杵']].倍率

        super().伤害指数计算()


class 极诣·阿修罗(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 极诣·阿修罗角色属性()
        self.角色属性A = 极诣·阿修罗角色属性()
        self.角色属性B = 极诣·阿修罗角色属性()
        self.一觉序号 = 极诣·阿修罗一觉序号
        self.二觉序号 = 极诣·阿修罗二觉序号
        self.三觉序号 = 极诣·阿修罗三觉序号
        self.护石选项 = deepcopy(极诣·阿修罗护石选项)
        self.符文选项 = deepcopy(极诣·阿修罗符文选项)
