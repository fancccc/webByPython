# 装备属性部分
# import json
# import os

from PublicReference.utils.constant import *
from .装备_套装 import *
from .装备_特殊 import *
from .装备_首饰 import *
from .装备_防具 import *
from .装备_武器 import *
from .基础函数 import *

装备版本 = "GF"

# with open("ResourceFiles/Config/release_version.json") as fp:
#     versionInfo = json.load(fp)
#     装备版本 = versionInfo['EquipmentVersion']
# fp.close()

# if 装备版本.upper() == "GF":

# else:
#     from .装备_武器_HF import *
#     from .装备_防具_HF import *
#     from .装备_首饰_HF import *
#     from .装备_特殊_HF import *
#     from .装备_套装_HF import *

class equipment():
    def __init__(self):
        self.load_equ()
        self.load_suit()

    def load_equ(self):
        self.equ_list = {}
        self.equ_id = {}
        self.equ_tuple = ()
        self.equ_id_tuple = ()
        self.index = {}
        for i in range(535): #534件装备
            temp = eval('装备{}()'.format(i))
            self.equ_list[i] = temp
            self.equ_id[temp.名称] = i
            self.equ_tuple += (temp,)
            self.equ_id_tuple += (i,)
            key = '{}\t{}\t{}'.format(temp.所属套装, temp.品质, temp.部位)
            self.index[key] = i

    def load_suit(self):
        self.suit_list = {}
        self.suit_id = {}
        self.suit_name = ()
        self.suit_tuple = ()
        for i in range(127): #126个套装效果
            temp = eval('套装效果{}()'.format(i))
            self.suit_list[i] = temp
            self.suit_tuple += (temp,)
            key = '{}[{}]'.format(temp.名称, temp.件数)
            self.suit_id[key] = i
            self.suit_name += (key,)

    def load_img(self):
        self.equ_img = {}
        for i in self.get_equ_id_list():
            path = './ResourceFiles/img/装备/{}.gif'.format(i)
            img = QMovie(path)
            img.start()
            self.equ_img[i] = img

    def get_suit_by_id(self, id):
        return self.suit_list.get(id, 套装())

    def get_suit_by_name(self, name):
        return self.get_suit_by_id(self.suit_id.get(name, 0))

    def get_equ_by_id(self, id):
        return self.equ_list.get(id, 装备())

    def get_img_by_id(self, id):
        return self.equ_img.get(id, QMovie(''))

    def get_equ_by_name(self, name):
        return self.get_equ_by_id(self.equ_id.get(name, 0))

    def get_img_by_name(self, name):
        return self.get_img_by_id(self.equ_id.get(name, 0))

    def get_id_by_name(self, name):
        return self.equ_id.get(name, 0)

    def get_equ_list(self):
        return self.equ_tuple

    def get_suit_list(self):
        return self.suit_tuple

    def get_equ_id_list(self):
        return self.equ_id_tuple

    def get_suit_name(self):
        return self.suit_name

    def get_id_by_index(self, suit, quality, part):
        key = '{}\t{}\t{}'.format(suit, quality, part)
        return self.index.get(key, 0)

    def get_equ_by_index(self, suit, quality, part):
        id = self.get_id_by_index(suit, quality, part)
        return self.get_equ_by_id(id)

equ = equipment()
