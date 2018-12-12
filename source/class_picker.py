# -*- coding: UTF-8 -*-

# Filename : class_atom.py
# author by : （学员ID)

# 要点： 巩固类的基本概念
#       巩固列表的使用方法（copy, remove, 以及两种不同的选取列表元素方式）
#       初步理解 try

# 配套练习：
#       try_picker.py

import random

# 引用物质表类
from class_matters_table import MattersTable


# 类定义
class Picker:

    # 内部属性
    _all_matters =[]
    _remained_matters = []

    # 定义构造方法
    def __init__(self):

        # 获取所有的物质类，并将其分子式转化为列表，存放在类的内部
        mt = MattersTable()

        self._all_matters = []
        for m in mt.matters_iterator:
            # print(m.formula)
            self._all_matters.append(m.formula)
        # print("Start: (%d)" % (len(self._all_matters)))

        # print(self._remained_matters)
        self._remained_matters = self._all_matters.copy()

        return

    # 从所有物质中随机挑选出， 除已挑选的物质以外的一个物质
    def pick_one(self, picked_list):

        # 定义返回值
        rtn = ''

        # print(self._remained_matters)
        # 仅当未挑选列表还有可供挑选的物质时才进行挑选，否则返回空值
        if len(self._remained_matters) > 0:

            # 将已挑选的物质一一排除
            for m in picked_list:
                try:
                    # print('Removed: %s' % (picked))
                    self._remained_matters.remove(m)
                except ValueError:
                    # print(m)
                    pass

            # 从剩下的物质中随机挑选一个新物质作为返回值
            # 方法一
            total = len(self._remained_matters)
            new_number = random.randrange(0, total)
            rtn = self._remained_matters[new_number]
            # print("Method-1 picked: %s" % (s))

            # 方法二
            rtn = random.choice(self._remained_matters)
            # print("Method-2 picked: %s" % (s))

            # 将新挑选的物质从未挑选列表中转移到已挑选列表
            self._remained_matters.remove(rtn)
            picked_list.append(rtn)

            # print("挑选了一个，还剩(%d)个" % (len(self._remained_matters)))

        return rtn


