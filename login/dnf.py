# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 23:26:42 2021

@author: Mario
"""

from PublicReference.common import *

def get_equ():
    equ = equipment()
    res = []
    for i in equ.get_suit_list():
        e = []
        for 品质 in ['神话', '史诗']:
            for 部位 in [
                    '上衣', '头肩', '下装', '鞋', '腰带', '项链', '手镯',
                    '戒指', '辅助装备', '魔法石', '耳环'
            ]:
                for j in equ.get_equ_id_list():
                    temp = equ.get_equ_by_id(j)
                    if temp.所属套装 == i.名称 and temp.品质 == 品质 and temp.部位 == 部位:
                        #res.append(e)
                        e.append([temp.所属套装, temp.品质, temp.部位, temp.名称, 
                                  'https://img-1259017984.cos.ap-nanjing.myqcloud.com/dnf/装备/%d.gif' % j])
                        #print(temp.所属套装, temp.品质, temp.部位, temp.名称, j)
        res.append(e)
        e = []
        if i.名称 == '能量主宰':
            break
    return res
res = get_equ()
'''
with open('equ.json','w')as f:
    f.write(str(equ))
for i in equ.get_suit_list():
    print(i.名称)
    if i.名称 == '能量主宰':
        break                   
'''