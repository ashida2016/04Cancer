# -*- coding: UTF-8 -*-

# Filename : class_picker.py
# author by : （学员ID)

# 要点： 巩固类的基本概念
#       巩固列表的使用方法（copy, remove, 以及两种不同的选取列表元素方式）
#       初步理解 try
#       初步理解 可更改的函数参数概念

# 配套练习：
#       try_picker.py

import random

# 引用物质类
from class_matter import Matter

# 引用物质表类
from class_matters_table import MattersTable


# 类定义
class Picker:

    # 内部属性
    _all_f = []
    _remained_f = []

    _all_m = MattersTable()
    # _remained_m = MattersTable()

    # 定义构造方法
    def __init__(self):

        # 获取所有的物质类，并将其分子式转化为列表，存放在类的内部
        _all_m = MattersTable()


        # 获取所有的物质分子式，组成列表
        self._all_f = []
        for m in _all_m.matters_iterator:
            # print(m.formula)
            self._all_f.append(m.formula)
        # print("Start: (%d)" % (len(self._all_f)))

        # print(self._remained_f)
        self._remained_f = self._all_f.copy()

        return

    # 从所有物质中随机挑选出 1 个物质， 排除已经挑选的物质
    # return 一个 matter 类
    def pick_one_matter(self, picked_matter_list):

        # 将已挑选的物质列表中的分子式挑选出来组成 新的列表
        # 【重要】新的列表中仅包含分子式
        picked_formula_list = []
        if not (picked_matter_list is None):
            for m in picked_matter_list:
                picked_formula_list.append(m.formula)

        # 重置剩余分子式列表，设置初始值为全部分子式
        self._remained_f = self._all_f.copy()

        # 将已挑选的物质 按分子式一一排除
        for f in picked_formula_list:
            try:
                # print('Removed: %s' % (picked))
                self._remained_f.remove(f)
            except ValueError:
                # print(f)
                pass

        # print(self._remained_f)
        # ---------

        # 定义返回值 - 一个空的 matter
        rtn_m = Matter()
        rtn_f = ''

        # 仅当未挑选分子式列表还有可供挑选的分子式时才进行挑选，否则返回空值
        if len(self._remained_f) > 0:

            # 从剩下的物质中随机挑选一个新物质作为返回值
            # 方法一
            total = len(self._remained_f)
            n = random.randrange(0, total)
            rtn_f = self._remained_f[n]
            # print("Method-1 picked: %s" % (s))

            # 方法二，用 choice 方法直接挑选（推荐方法）
            rtn_f = random.choice(self._remained_f)
            # print("Method-2 picked: %s" % (s))

            # 将新挑选的物质从未挑选列表中转移到已挑选列表
            # 从剩余分子式列表中删除
            self._remained_f.remove(rtn_f)
            # 将删除的分子式转化为类，加入传入参数
            rtn_m = self._all_m.get_matter_by_formula(rtn_f)
            # 将本次挑选的matter类添加到 已完成列表中去
            picked_matter_list.append(rtn_m)

            # print("挑选了一个，还剩(%d)个" % (len(self._remained_f)))

        return rtn_m

    # 从所有物质中随机挑选出 1 个物质， 排除已经挑选的物质
    def pick_one(self, picked_formula_list):

        # 定义返回值
        rtn = ''

        # 剩余列表设置初始值为全部物质
        self._remained_f = self._all_f.copy()

        # 将已挑选的物质一一排除
        for f in picked_formula_list:
            try:
                # print('Removed: %s' % (picked))
                self._remained_f.remove(f)
            except ValueError:
                # print(f)
                pass

        # print(self._remained_f)
        # 仅当未挑选列表还有可供挑选的物质时才进行挑选，否则返回空值
        if len(self._remained_f) > 0:

            # 从剩下的物质中随机挑选一个新物质作为返回值
            # 方法一
            total = len(self._remained_f)
            new_number = random.randrange(0, total)
            rtn = self._remained_f[new_number]
            # print("Method-1 picked: %s" % (s))

            # 方法二
            rtn = random.choice(self._remained_f)
            # print("Method-2 picked: %s" % (s))

            # 将新挑选的物质从未挑选列表中转移到已挑选列表
            self._remained_f.remove(rtn)
            picked_formula_list.append(rtn)

            # print("挑选了一个，还剩(%d)个" % (len(self._remained_f)))

        return rtn

    # 从所有物质中随机+不重复的挑选出 n 个物质
    def pick_many(self, picked_formula_list, times):

        # 定义返回物质列表
        rtn_matter_list = []

        for i in range(times):

            # 挑选一次
            f_new_pick = self.pick_one(picked_formula_list)
            # 将已经挑选出来的物质分子式 加入 已挑出的列表内 - 为下次挑选做准备
            # picked_formula_list.append(f_new_pick)

            # 用挑选出来的分子式去寻找物质
            # m_picked = mt.get_matter_by_formula(f_new_pick)

            m_picked = self._all_m.get_matter_by_formula(f_new_pick)

            # 将挑选出来的物质类添加到返回列表中去
            rtn_matter_list.append(m_picked)

        return rtn_matter_list


