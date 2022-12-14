from math import *
from PublicReference.base import *

# 2020.7.3  数据有待修整
# 2020.9.20 加入新护石，改为三觉版本

# 武器战斧
# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '战斧':
#             return round(self.CD / self.恢复 * 1.1, 1)

class 职业主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    data0 = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []

    攻击次数4 = 0
    攻击次数5 = 0
    攻击次数6 = 0
    攻击次数7 = 0

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
        if len(self.data4) >= self.等级 and len(self.data4) > 0:
            等效倍率 += self.data4[self.等级] * self.攻击次数5
        if len(self.data5) >= self.等级 and len(self.data5) > 0:
            等效倍率 += self.data5[self.等级] * self.攻击次数6
        if len(self.data6) >= self.等级 and len(self.data6) > 0:
            等效倍率 += self.data6[self.等级] * self.攻击次数7
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率

# 战斧精通
class 技能0(被动技能):
    名称 = '战斧精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1.05 + 0.01 * self.等级, 5)
        else :
            return round(0.95 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

# 一觉被动
class 技能1(被动技能):
    名称 = '异端烙印'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)


# 二觉被动
class 技能2(被动技能):
    名称 = '定罪法则'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)
    关联技能2 = ['火焰精华']#此处删除神焰
    def 加成倍率2(self, 武器类型):
        if self.等级 ==0:
            return 1.0
        else:
            return(round(1.073 + 0.017 * self.等级, 5)/ self.加成倍率(武器类型))
    冷却关联技能 = ['火焰精华','神焰']
    def CD缩减倍率(self, 武器类型):
        if  self.等级 ==0:
            return 1.0
        else:
            return 0.85

# 三觉被动
class 技能3(被动技能):
    名称 = '狂炎告解'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 惩戒十字
class 技能4(职业主动技能):
    名称 = '惩戒十字'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    #基础 = 1186 + 1779 - 120 - 180
    #成长 = 300
    data0 = [ int(i*1.0) for i in [0,1198, 1321, 1442, 1564, 1685, 1809, 1929, 2052, 2173, 2296, 2416, 2540, 2660, 2783, 2903, 3027, 3147, 3268, 3391, 3512, 3634, 3755, 3878, 3999, 4121, 4243, 4365, 4486, 4610, 4730, 4853, 4973, 5097, 5217, 5340, 5461, 5584, 5704, 5825, 5948, 6069, 6191, 6313, 6435, 6556, 6679, 6800, 6922, 7043, 7166, 7287, 7410, 7531, 7654, 7774, 7898, 8018, 8141, 8261, 8383, 8505, 8626, 8749, 8870, 8992, 9113, 9236, 9357, 9479, 9601]]
    攻击次数 = 1
    data1 = [ int(i*1.0) for i in [0,1800, 1982, 2165, 2347, 2531, 2713, 2895, 3078, 3260, 3444, 3626, 3809, 3991, 4175, 4357, 4539, 4722, 4904, 5088, 5270, 5453, 5635, 5819, 6001, 6183, 6366, 6548, 6732, 6914, 7097, 7279, 7461, 7645, 7827, 8010, 8192, 8376, 8558, 8741, 8923, 9105, 9289, 9471, 9654, 9836, 10019, 10202, 10385, 10567, 10749, 10933, 11115, 11298, 11480, 11663, 11846, 12029, 12211, 12393, 12577, 12759, 12942, 13124, 13307, 13490, 13673, 13855, 14037, 14220, 14403]]
    攻击次数1 = 1
    CD = 6
    TP成长 = 0.10
    TP上限 = 5

# 净化火焰瓶
class 技能5(职业主动技能):
    名称 = '净化火焰瓶'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    #基础 = 2938 - 298
    #成长 = 298
    data0 = [ int(i*1.0) for i in [0, 2938, 3236, 3535, 3833, 4131, 4429, 4727, 5025, 5323, 5621, 5920, 6218, 6516, 6814, 7112, 7410, 7708, 8007, 8305, 8603, 8901, 9199, 9497, 9795, 10094, 10392, 10690, 10988, 11286, 11584, 11882, 12180, 12479, 12777, 13075, 13373, 13671, 13969, 14267, 14566, 14864, 15162, 15460, 15758, 16056, 16354, 16653, 16951, 17249, 17547, 17845, 18143, 18441, 18739, 19038, 19336, 19634, 19932, 20230, 20528, 20826, 21125, 21423, 21721, 22019, 22317, 22615, 22913, 23212, 23510]]
    CD = 6
    TP成长 = 0.10
    TP上限 = 5

# 裁决之击
class 技能6(职业主动技能):
    名称 = '裁决之击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    #基础 = 4449 - 451.5
    #成长 = 451.5
    data0 = [ int(i*1.0) for i in [0,4449, 4901, 5352, 5803, 6256, 6707, 7158, 7609, 8060, 8512, 8964, 9415, 9866, 10319, 10770, 11222, 11673, 12123, 12577, 13027, 13478, 13930, 14382, 14833, 15285, 15736, 16188, 16640, 17090, 17541, 17993, 18445, 18896, 19348, 19799, 20252, 20703, 21154, 21604, 22058, 22508, 22960, 23411, 23862, 24315, 24766, 25217, 25669, 26121, 26573, 27023, 27474, 27927, 28378, 28829, 29281, 29732, 30184, 30636, 31086, 31537, 31990, 32441, 32892, 33344, 33795, 34247, 34699, 35150, 35600]]
    CD = 8
    TP成长 = 0.10
    TP上限 = 5
    #倍率 = 1*1.134，弃，2020年11月29日微调


# 火焰精华
class 技能7(职业主动技能):
    名称 = '火焰精华'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 29
    #基础 = 4315 - 688
    #成长 = 688
    data0 = [ int(i*1.0) for i in [0, 4315, 5003, 5691, 6378, 7066, 7754, 8442, 9130, 9818, 10506, 11194, 11882, 12570, 13258, 13946, 14634, 15321, 16009, 16697, 17385, 18073, 18761, 19449, 20137, 20825, 21513, 22201, 22889, 23577, 24264, 24952, 25640, 26328, 27016, 27704, 28392, 29080, 29768, 30456, 31144, 31832, 32520, 33207, 33895, 34583, 35271, 35959, 36647, 37335, 38023, 38711, 39399, 40087, 40775, 41463, 42150, 42838, 43526, 44214, 44902, 45590, 46278, 46966, 47654, 48342, 49030, 49718, 50406, 51093, 51781]]
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

# 神焰
# 三觉版本改版，tp为基础精通
class 技能8(主动技能):
    名称 = '神焰'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    基础 = 2416*9.452#补基础精通
    成长 = 0
    CD = 10
    TP成长 = 0.10
    TP上限 = 3
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1.05 + 0.01 * self.等级, 2)
        else:
            return round(1.15 + 0.02 * (self.等级 - 10), 2)

# 审判重击
class 技能9(职业主动技能):
    名称 = '审判重击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    #基础 = 2852 + 3032 - 290 - 307
    #成长 = 290 + 307
    data0 = [ int(i*1.0) for i in [0,2852, 3143, 3432, 3721, 4012, 4301, 4590, 4879, 5168, 5458, 5748, 6037, 6326, 6617, 6906, 7196, 7486, 7775, 8064, 8353, 8642, 8933, 9222, 9511, 9801, 10091, 10380, 10671, 10960, 11249, 11538, 11827, 12118, 12407, 12696, 12986, 13275, 13564, 13855, 14145, 14434, 14723, 15012, 15303, 15592, 15881, 16170, 16460, 16749, 17039, 17330, 17619, 17908, 18197, 18486, 18777, 19066, 19355, 19645, 19934, 20224, 20513, 20804, 21093, 21382, 21671, 21962, 22251, 22540, 22829]]
    攻击次数 = 1
    data1 = [ int(i*1.0) for i in [0,3032, 3338, 3646, 3953, 4261, 4570, 4877, 5185, 5492, 5799, 6107, 6414, 6723, 7031, 7337, 7645, 7953, 8260, 8569, 8877, 9183, 9491, 9798, 10106, 10415, 10722, 11030, 11338, 11644, 11952, 12259, 12568, 12876, 13182, 13490, 13798, 14105, 14413, 14722, 15028, 15336, 15643, 15951, 16259, 16566, 16875, 17183, 17489, 17797, 18104, 18412, 18721, 19027, 19335, 19643, 19950, 20258, 20565, 20874, 21181, 21488, 21796, 22104, 22411, 22719, 23028, 23334, 23642, 23949, 24257]]
    攻击次数2 = 1
    CD = 10
    TP成长 = 0.10
    TP上限 = 5
    #倍率 = round((1/1.081)*1.129,8)，弃

# 神焰斩
class 技能10(职业主动技能):
    名称 = '神焰斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36

    #基础 = 1209  - 123
    #成长 = 123
    data0 = [ int(i*1.0) for i in [0, 1209, 1332, 1455, 1578, 1700, 1823, 1946, 2069, 2191, 2314, 2437, 2560, 2682, 2805, 2928, 3051, 3173, 3296, 3419, 3542, 3664, 3787, 3910, 4033, 4155, 4278, 4401, 4524, 4647, 4769, 4892, 5015, 5138, 5260, 5383, 5506, 5629, 5751, 5874, 5997, 6120, 6242, 6365, 6488, 6611, 6733, 6856, 6979, 7102, 7224, 7347, 7470, 7593, 7715, 7838, 7961, 8084, 8206, 8329, 8452, 8575, 8697, 8820, 8943, 9066, 9188, 9311, 9434, 9557, 9679]]
    攻击次数 = 1

    #基础2 = 10903 -1106
    #成长2 = 1106
    攻击次数2 = 1
    data1 = [ int(i*1.0) for i in [0, 10903, 12009, 13116, 14222, 15328, 16434, 17540, 18646, 19753, 20859, 21965, 23071, 24177, 25284, 26390, 27496, 28602, 29708, 30814, 31921, 33027, 34133, 35239, 36345, 37451, 38558, 39664, 40770, 41876, 42982, 44089, 45195, 46301, 47407, 48513, 49619, 50726, 51832, 52938, 54044, 55150, 56256, 57363, 58469, 59575, 60681, 61787, 62893, 64000, 65106, 66212, 67318, 68424, 69531, 70637, 71743, 72849, 73955, 75061, 76168, 77274, 78380, 79486, 80592, 81698, 82805, 83911, 85017, 86123, 87229]]
    # 默认武器处于点火状态，怪物处于焚烧状态，否则data1 = [0, 10889, 11994, 13099, 14204, 15308, 16413, 17518, 18623, 19727, 20832, 21937, 23042, 24146, 25251, 26356, 27461, 28565, 29670, 30775, 31880, 32984, 34089, 35194, 36299, 37403, 38508, 39613, 40718, 41823, 42927, 44032, 45137, 46242, 47346, 48451, 49556, 50661, 51765, 52870, 53975, 55080, 56184, 57289, 58394, 59499, 60603, 61708, 62813, 63918, 65022, 66127, 67232, 68337, 69441, 70546, 71651, 72756, 73860, 74965, 76070, 77175, 78280, 79384, 80489, 81594, 82699, 83803, 84908, 86013, 87118]
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.攻击次数2 = 1.29
            self.CD *= 0.85
        elif x == 1:
            self.攻击次数 = 0
            self.攻击次数2 = 1.38
            self.CD *= 0.85

# 神焰洗礼
class 技能11(职业主动技能):
    名称 = '神焰洗礼'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    #基础 = 9139 - 928
    data0 = [ int(i*1.0) for i in [0,9139, 10067, 10996, 11922, 12850, 13777, 14705, 15631, 16559, 17486, 18412, 19340, 20269, 21196, 22124, 23050, 23978, 24905, 25831, 26759, 27687, 28615, 29543, 30469, 31397, 32324, 33251, 34178, 35106, 36032, 36961, 37888, 38816, 39743, 40670, 41597, 42525, 43451, 44379, 45307, 46235, 47162, 48089, 49016, 49944, 50870, 51798, 52725, 53654, 54581, 55508, 56435, 57363, 58289, 59217, 60144, 61072, 61998, 62927, 63854, 64782, 65708, 66636, 67563, 68491, 69417, 70345, 71273, 72201, 73127]]
    #2020年11月29日微调
    #成长 = 928
    CD = 15
    TP成长 = 0.10
    TP上限 = 5


# 神焰怒火
class 技能12(职业主动技能):
    名称 = '神焰怒火'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    data0 = [0,1687, 1859, 2030, 2202, 2372, 2544, 2715, 2887, 3059, 3230, 3401, 3571, 3743, 3915, 4086, 4258, 4428, 4600, 4772, 4943, 5115, 5284, 5456, 5627, 5799, 5971, 6142, 6313, 6484, 6656, 6828, 6999, 7171, 7340, 7512, 7684, 7855, 8027, 8198, 8369, 8540, 8712, 8884, 9055, 9227, 9396, 9568, 9740, 9911, 10083, 10254, 10425, 10596, 10768, 10940, 11110, 11281, 11452, 11624, 11796, 11967, 12139, 12309, 12481, 12653, 12824, 12995, 13166, 13337, 13508]
    攻击次数 = 5

    data1 = [0,5627, 6200, 6770, 7340, 7912, 8483, 9055, 9625, 10197, 10768, 11338, 11910, 12481, 13052, 13623, 14195, 14765, 15336, 15908, 16479, 17050, 17621, 18193, 18763, 19333, 19906, 20475, 21047, 21618, 22189, 22760, 23331, 23903, 24473, 25045, 25616, 26187, 26758, 27329, 27900, 28471, 29043, 29614, 30185, 30756, 31327, 31898, 32469, 33041, 33611, 34183, 34753, 35323, 35895, 36466, 37038, 37608, 38180, 38751, 39321, 39893, 40464, 41035, 41606, 42178, 42748, 43319, 43891, 44462, 45033]
    攻击次数2 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.85
            self.攻击次数 += 2
        elif x == 1:
            self.CD *= 0.85
            self.攻击次数 += 2
            self.倍率 *= 1.09


# 行刑
class 技能13(职业主动技能):
    名称 = '行刑'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    #基础 = 23205 -2354.5
    #成长 = 2354.5
    data0 = [ int(i*1.0) for i in [0, 23205, 25560, 27914, 30268, 32622, 34977, 37331, 39685, 42039, 44394, 46748, 49102, 51456, 53810, 56165, 58519, 60873, 63227, 65582, 67936, 70290, 72644, 74998, 77353, 79707, 82061, 84415, 86770, 89124, 91478, 93832, 96187, 98541, 100895, 103249, 105603, 107958, 110312, 112666, 115020, 117375, 119729, 122083, 124437, 126791, 129146, 131500, 133854, 136208, 138563, 140917, 143271, 145625, 147980, 150334, 152688, 155042, 157396, 159751, 162105, 164459, 166813, 169168, 171522, 173876, 176230, 178584, 180939, 183293, 185647]]
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    是否装备护石 = 0

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.9
            self.是否装备护石 = 1
        elif x == 1:
            self.CD *= 0.9
            self.是否装备护石 = 2

#数据未录
# 一觉
class 技能14(职业主动技能):
    名称 = '火刑'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    #多段
    #基础 = 10371 - 678 *12
    #成长 = 678
    #前2
    #基础2 = 9712 + 29135 - 12 *(633+1901)
    #成长2 = 633 +1901
    data0 = [ int(i*1.0) for i in [0, 2735, 3368, 4003, 4638, 5271, 5906, 6541, 7174, 7809, 8442, 9077, 9712, 10345, 10980, 11613, 12248, 12883, 13516, 14151, 14784, 15419, 16054, 16687, 17322, 17955, 18590, 19225, 19858, 20493, 21127, 21761, 22396, 23030, 23664, 24299, 24932, 25567, 26201, 26835, 27470, 28104, 28738, 29372, 30006, 30641, 31275, 31909, 32543, 33178, 33812, 34446, 35081, 35714, 36349, 36983, 37617, 38252, 38885, 39520, 40155, 40788, 41423, 42057, 42691, 43326, 43959, 44594, 45229, 45862]]
    攻击次数 = 1
    data1 = [ int(i*1.0) for i in [0, 8205, 10107, 12010, 13913, 15816, 17719, 19622, 21523, 23426, 25329, 27232, 29135, 31036, 32939, 34842, 36745, 38648, 40551, 42453, 44356, 46259, 48162, 50064, 51966, 53869, 55772, 57675, 59578, 61481, 63382, 65285, 67188, 69091, 70994, 72897, 74799, 76702, 78604, 80507, 82410, 84312, 86215, 88118, 90021, 91924, 93827, 95728, 97631, 99534, 101437, 103340, 105242, 107144, 109047, 110950, 112853, 114756, 116658, 118561, 120464, 122367, 124270, 126172, 128074, 129977, 131880, 133783, 135686, 137587]]
    攻击次数2= 1
    data2 = [ int(i*1.0) for i in [0, 2920, 3597, 4276, 4953, 5630, 6307, 6985, 7662, 8339, 9016, 9694, 10371, 11049, 11727, 12404, 13081, 13758, 14435, 15113, 15790, 16467, 17146, 17823, 18500, 19177, 19855, 20532, 21209, 21886, 22563, 23241, 23919, 24596, 25274, 25951, 26628, 27305, 27983, 28660, 29337, 30015, 30693, 31370, 32047, 32724, 33402, 34079, 34756, 35433, 36111, 36789, 37466, 38143, 38821, 39498, 40175, 40852, 41530, 42207, 42884, 43563, 44240, 44917, 45594, 46271, 46949, 47626, 48303, 48980]]
    攻击次数3 = 15

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if self.等级 >=6:
            self.攻击次数3 *= 1.1
        return super().等效百分比(武器类型)
    CD = 145


# 神焰漩涡,最大旋转
class 技能15(职业主动技能):
    名称 = '神焰漩涡'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    data0 =[0,1639, 1805, 1972, 2139, 2304, 2471, 2637, 2803, 2970, 3136, 3302, 3470, 3635, 3803, 3968, 4134, 4301, 4468, 4634, 4801, 4967, 5132, 5299, 5465, 5633, 5799, 5965, 6132, 6298, 6463, 6630, 6796, 6963, 7130, 7296, 7463, 7629, 7794, 7961, 8128, 8294, 8461, 8627, 8793, 8960, 9125, 9294, 9459, 9625, 9792, 9958, 10124, 10292, 10458, 10623, 10790, 10956, 11122, 11289, 11455, 11623, 11789, 11954, 12121, 12287, 12453, 12620, 12787, 12953, 13120]
    攻击次数 = 9

    data1 = [0,3461, 3813, 4164, 4515, 4866, 5218, 5569, 5920, 6271, 6622, 6974, 7325, 7677, 8027, 8378, 8730, 9081, 9433, 9783, 10136, 10486, 10837, 11189, 11539, 11892, 12242, 12594, 12945, 13295, 13648, 13998, 14351, 14701, 15053, 15404, 15756, 16107, 16457, 16809, 17160, 17512, 17863, 18215, 18565, 18916, 19268, 19619, 19971, 20321, 20673, 21024, 21375, 21727, 22077, 22429, 22780, 23132, 23483, 23833, 24185, 24536, 24888, 25239, 25591, 25941, 26293, 26644, 26995, 27347, 27697]
    攻击次数2 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 += 3
            self.攻击次数 *= 0.94
            self.攻击次数2 *= 1.14
        elif x == 1:
            self.攻击次数 += 3
            self.攻击次数 *= 1.01######
            self.攻击次数2 *= 1.14

# 净化之焰

class 技能16(职业主动技能):
    名称 = '净化之焰'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18

    #基础 = 28032 - 2844
    #成长 = 2844
    data0 = [ int(i*1.0) for i in [0, 28032, 30875, 33719, 36563, 39407, 42251, 45095, 47938, 50782, 53626, 56470, 59314, 62158, 65001, 67845, 70689, 73533, 76377, 79221, 82064, 84908, 87752, 90596, 93440, 96284, 99127, 101971, 104815, 107659, 110503, 113347, 116190, 119034, 121878, 124722, 127566, 130410, 133254, 136097, 138941, 141785, 144629, 147473, 150317, 153160, 156004, 158848, 161692, 164536, 167380, 170223, 173067, 175911, 178755, 181599, 184443, 187286, 190130, 192974, 195818, 198662, 201506, 204349, 207193, 210037, 212881, 215725, 218569, 221412, 224256]]
    CD = 40
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.27#####

# 裁决轮回斩
class 技能17(职业主动技能):
    名称 = '裁决轮回斩'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16

    data0 = [0,2873, 3165, 3456, 3749, 4040, 4332, 4623, 4916, 5207, 5499, 5790, 6081, 6373, 6665, 6956, 7248, 7540, 7832, 8123, 8415, 8707, 8999, 9290, 9582, 9874, 10164, 10456, 10747, 11039, 11331, 11623, 11914, 12206, 12498, 12790, 13081, 13373, 13665, 13957, 14247, 14539, 14830, 15123, 15414, 15706, 15997, 16290, 16581, 16873, 17164, 17457, 17748, 18040, 18330, 18621, 18914, 19205, 19497, 19788, 20081, 20372, 20664, 20955, 21248, 21539, 21831, 22122, 22413, 22705, 22996]
    攻击次数 = 3
    data1 = [0,45777, 50423, 55067, 59712, 64356, 68999, 73643, 78289, 82933, 87576, 92221, 96865, 101511, 106155, 110798, 115442, 120087, 124731, 129375, 134020, 138664, 143309, 147953, 152596, 157241, 161886, 166530, 171173, 175818, 180463, 185108, 189751, 194395, 199040, 203685, 208329, 212972, 217617, 222261, 226907, 231550, 236194, 240839, 245483, 250127, 254770, 259416, 264060, 268705, 273348, 277992, 282638, 287282, 291926, 296569, 301214, 305859, 310504, 315147, 319791, 324436, 329080, 333725, 338369, 343013, 347657, 352302, 356945, 361590, 366235]
    攻击次数2 = 1

    CD = 40

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 -= 1
            self.攻击次数2 *= 1.26
            self.CD *= 0.92
            self.攻击次数 *= 1.37



# 车轮刑
class 技能18(职业主动技能):
    名称 = '车轮刑'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    #基础 = (1872 - 190)*26 +12016 - 1219
    #成长 = 190 *26 + 1219
    data0 = [ int(i*1.0) for i in [0,1873, 2063, 2252, 2443, 2633, 2823, 3013, 3204, 3393, 3583, 3774, 3963, 4154, 4344, 4533, 4724, 4914, 5104, 5294, 5485, 5674, 5864, 6055, 6244, 6435, 6625, 6814, 7005, 7195, 7385, 7575, 7766, 7955, 8145, 8336, 8528, 8717, 8907, 9098, 9287, 9478, 9668, 9857, 10048, 10238, 10428, 10618, 10809, 10998, 11188, 11379, 11568, 11759, 11949, 12138, 12329, 12519, 12709, 12899, 13090, 13279, 13469, 13660, 13849, 14040, 14230, 14419, 14610, 14800, 14990]]
    攻击次数 = 1
    data1 = [ int(i*1.0) for i in [0,1873, 2063, 2252, 2443, 2633, 2823, 3013, 3204, 3393, 3583, 3774, 3963, 4154, 4344, 4533, 4724, 4914, 5104, 5294, 5485, 5674, 5864, 6055, 6244, 6435, 6625, 6814, 7005, 7195, 7385, 7575, 7766, 7955, 8145, 8336, 8528, 8717, 8907, 9098, 9287, 9478, 9668, 9857, 10048, 10238, 10428, 10618, 10809, 10998, 11188, 11379, 11568, 11759, 11949, 12138, 12329, 12519, 12709, 12899, 13090, 13279, 13469, 13660, 13849, 14040, 14230, 14419, 14610, 14800, 14990]]
    攻击次数2 = 25
    data2 = [ int(i*1.0) for i in [0,12021, 13242, 14460, 15681, 16900, 18119, 19340, 20559, 21779, 22998, 24219, 25437, 26658, 27878, 29096, 30317, 31536, 32756, 33975, 35196, 36415, 37635, 38855, 40073, 41294, 42512, 43733, 44953, 46173, 47392, 48612, 49832, 51050, 52271, 53491, 54710, 55930, 57149, 58369, 59590, 60809, 62028, 63248, 64468, 65687, 66907, 68128, 69346, 70567, 71785, 73005, 74225, 75445, 76665, 77884, 79105, 80323, 81544, 82762, 83982, 85203, 86422, 87642, 88861, 90082, 91300, 92521, 93741, 94959, 96180]]
    攻击次数3= 1
    CD = 45

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.31

# 二觉
class 技能19(职业主动技能):
    名称 = '炎狱祭坛：炮烙'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    #基础 = (33499 - 4030*5) *3 + 150746 - 18135*5
    data0 = [ int(i*1.0) for i in [0,17463, 21512, 25561, 29610, 33660, 37710, 41758, 45808, 49857, 53908, 57957, 62007, 66055, 70105, 74155, 78205, 82254, 86302, 90352, 94402, 98452, 102501, 106551, 110599, 114650, 118699, 122749, 126798, 130847, 134897]]
    攻击次数 = 3
    data1 = [ int(i*1.0) for i in [0,78584, 96806, 115029, 133252, 151474, 169696, 187921, 206142, 224365, 242588, 260810, 279033, 297255, 315478, 333701, 351922, 370145, 388367, 406590, 424814, 443037, 461259, 479482, 497704, 515927, 534150, 552371, 570594, 588816, 607039]]
    攻击次数1 = 1
    #成长 = 4030 *3 + 18135
    CD = 180
    #倍率 = round((1/1.127)*1.132,8)

# 95
class 技能20(职业主动技能):
    名称 = '补赎逆十字'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6

    data0 =[0,44324, 48821, 53317, 57814, 62311, 66807, 71304, 75801, 80298, 84794, 89291, 93788, 98284, 102781, 107278, 111774, 116271, 120768, 125264, 129761, 134258, 138755, 143251, 147748, 152245, 156741, 161238, 165735, 170231, 174728, 179225, 183721, 188218, 192715, 197211, 201708, 206205, 210702, 215198, 219695, 224192, 228688, 233185, 237682, 242178, 246675, 251172, 255668, 260165, 264662, 269159, 273655, 278152, 282649, 287145, 291642, 296139, 300635, 305132, 309629]
    攻击次数 = 1

    data1 = [0,55405, 61026, 66647, 72268, 77889, 83509, 89130, 94751, 100372, 105993, 111614, 117235, 122855, 128476, 134097, 139718, 145339, 150960, 156581, 162202, 167822, 173443, 179064, 184685, 190306, 195927, 201548, 207168, 212789, 218410, 224031, 229652, 235273, 240894, 246514, 252135, 257756, 263377, 268998, 274619, 280240, 285861, 291481, 297102, 302723, 308344, 313965, 319586, 325207, 330827, 336448, 342069, 347690, 353311, 358932, 364553, 370173, 375794, 381415, 387036]
    攻击次数2 = 1

    data2 = [0,554, 610, 666, 722, 778, 835, 891, 947, 1003, 1059, 1116, 1172, 1228, 1284, 1340, 1397, 1453, 1509, 1565, 1622, 1678, 1734, 1790, 1846, 1903, 1959, 2015, 2071, 2127, 2184, 2240, 2296, 2352, 2408, 2465, 2521, 2577, 2633, 2689, 2746, 2802, 2858, 2914, 2971, 3027, 3083, 3139, 3195, 3252, 3308, 3364, 3420, 3476, 3533, 3589, 3645, 3701, 3757, 3814, 3870]
    攻击次数3 = 20 +20

    CD = 60

# 三觉
class 技能21(职业主动技能):
    名称 = '无间狱·焚罪'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    data0 =[0,37813, 46582, 55350, 64119, 72887, 81656, 90424, 99193, 107961, 116730, 125498, 134266, 143035, 151803, 160572, 169340, 178109, 186877, 195646, 204414, 213183, 221951, 230719, 239488, 248256, 257025, 265793, 274562, 283330, 292099, 300867, 309635, 318404, 327172, 335941, 344709, 353478, 362246, 371015, 379783, 388552, 397320, 406088, 414857, 423625, 432394, 441162, 449931, 458699, 467468, 476236, 485005, 493773, 502541, 511310, 520078, 528847, 537615, 546384, 555152]
    攻击次数 = 1
    data1 = [0,15125, 18632, 22140, 25647, 29155, 32662, 36169, 39677, 43184, 46692, 50199, 53706, 57214, 60721, 64228, 67736, 71243, 74751, 78258, 81765, 85273, 88780, 92287, 95795, 99302, 102810, 106317, 109824, 113332, 116839, 120347, 123854, 127361, 130869, 134376, 137883, 141391, 144898, 148406, 151913, 155420, 158928, 162435, 165942, 169450, 172957, 176465, 179972, 183479, 186987, 190494, 194002, 197509, 201016, 204524, 208031, 211538, 215046, 218553, 222061]
    攻击次数2 = 10
    data2 = [0,189069, 232912, 276754, 320596, 364438, 408281, 452123, 495965, 539807, 583650, 627492, 671334, 715176, 759019, 802861, 846703, 890545, 934388, 978230, 1022072, 1065914, 1109757, 1153599, 1197441, 1241284, 1285126, 1328968, 1372810, 1416653, 1460495, 1504337, 1548179, 1592022, 1635864, 1679706, 1723548, 1767391, 1811233, 1855075, 1898917, 1942760, 1986602, 2030444, 2074287, 2118129, 2161971, 2205813, 2249656, 2293498, 2337340, 2381182, 2425025, 2468867, 2512709, 2556551, 2600394, 2644236, 2688078, 2731920, 2775763]
    攻击次数3 = 1
    CD = 290
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0



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

神启·异端审判者一觉序号 = 0
神启·异端审判者二觉序号 = 0
神启·异端审判者三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        神启·异端审判者一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        神启·异端审判者二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        神启·异端审判者三觉序号 = 技能序号[i.名称]

神启·异端审判者护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        神启·异端审判者护石选项.append(i.名称)

神启·异端审判者符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        神启·异端审判者符文选项.append(i.名称)


class 神启·异端审判者角色属性(角色属性):
    实际名称 = '神启·异端审判者'
    角色 = '圣职者(女)'
    职业 = '异端审判者'

    武器选项 = ['战斧']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量']

    主BUFF = 1.93

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if self.次数输入[self.技能序号[i.名称]] == '/CD':
                    技能释放次数.append(int((self.时间输入 - i.演出时间) / i.等效CD(self.武器类型,self.类型) + 1 + i.基础释放次数))
                elif self.次数输入[self.技能序号[i.名称]] != '0':
                    技能释放次数.append(round(float(self.次数输入[self.技能序号[i.名称]]),2))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)

        if '行刑' in [self.护石第一栏, self.护石第二栏, self.护石第三栏] and self.次数输入[self.技能序号['神焰']] == '/CD':
            技能释放次数[self.技能序号['神焰']] += 技能释放次数[self.技能序号['行刑']]

        return 技能释放次数

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['火焰精华']].被动倍率 /= self.技能栏[self.技能序号['神焰']].加成倍率(self.武器类型)
        if self.技能栏[self.技能序号['行刑']].是否装备护石 == 1:
            self.技能栏[self.技能序号['行刑']].被动倍率 /= self.技能栏[self.技能序号['神焰']].加成倍率(self.武器类型)
            self.技能栏[self.技能序号['行刑']].被动倍率 *= 1 + (self.技能栏[self.技能序号['神焰']].加成倍率(self.武器类型) - 1) * 1.39
        elif self.技能栏[self.技能序号['行刑']].是否装备护石 == 2:
            self.技能栏[self.技能序号['行刑']].被动倍率 /= self.技能栏[self.技能序号['神焰']].加成倍率(self.武器类型)
            self.技能栏[self.技能序号['行刑']].被动倍率 *= 1 + (self.技能栏[self.技能序号['神焰']].加成倍率(self.武器类型) - 1) * 2.00


class 神启·异端审判者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 神启·异端审判者角色属性()
        self.角色属性A = 神启·异端审判者角色属性()
        self.角色属性B = 神启·异端审判者角色属性()
        self.一觉序号 = 神启·异端审判者一觉序号
        self.二觉序号 = 神启·异端审判者二觉序号
        self.三觉序号 = 神启·异端审判者三觉序号
        self.护石选项 = deepcopy(神启·异端审判者护石选项)
        self.符文选项 = deepcopy(神启·异端审判者符文选项)

