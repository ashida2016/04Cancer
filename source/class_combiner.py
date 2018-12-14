# -*- coding: UTF-8 -*-

# Filename : class_combiner.py
# author by : （学员ID)

# 要点： 巩固类的基本概念

# 配套练习：
#       try_combiner.py

import random
# 引用物质类
from class_atoms_table import AtomsTable

# 引用物质类
from class_matter import Matter

# 引用 copy 类
import copy


class Combiner:

    def __init__(self):
        return

    def mix2(self, a, m1, b, m2):

        e1 = m1.get_elements()
        e2 = m2.get_elements()

        # 将两个原子字典合并为 1 个
        # 先将 e1 全盘复制过来，并乘以 份数a
        e_merged = {}
        for key, value in e1.items():
            new_value = a * value
            e_merged.update({key: new_value})

        # 将 e2 中的 key 合并，如果 e1 中已经有的，则 value 相加
        for key, value in e2.items():
            if key in e_merged.keys():
                new_value = e_merged[key] + b * value
            else:
                new_value = b * value
            e_merged.update({key: new_value})

        rtn_e = sorted(e_merged.items(), key=lambda x: x[0], reverse=False)

        return rtn_e

    def make_formula_of2(self, a, m1, b, m2):

        if a > 1:
            s1 = str(a) + m1.formula
        else:
            s1 = m1.formula

        if b > 1:
            s2 = str(b) + m2.formula
        else:
            s2 = m2.formula

        sf = s1 + " + " + s2
        return sf