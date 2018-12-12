# -*- coding: UTF-8 -*-

# Filename : class_matter.py
# author by : （学员ID)

# 目的： 学会在一个类中使用其他类
#       加深类的使用方法
#       加深理解函数返回值的使用
# 配套练习：
#       try_class3.py


import random

# 引用元素周期表类
from class_atoms_table import AtomsTable

# 引用分解工具类
from class_tool_split_to_elements import SplitToElements


# 类定义
class Matter:

    # 定义类基本属性（可公开被外部直接调用）
    name = 'Unkown'                 # 物质的中文名称
    alias = 'Unkown'                # 物质的别名
    formula = 'Unkown'              # 物质的化学分子式
    catalog1 = 'Unkown'             # 分类1
    comment = 'Unkown'              # 物质简介

    __elements = {}                  # 元素字典  - 比较复杂，不求掌握
    __mass = -1.0                    # 分子量    - 根据元素字典来计算

    _price = 0.0                    # 当前价格 - 将来动态的获取，目前暂时用 random 替代

    #__atoms_table = AtomsTable()     # 内部计算用的 元素

    def __init__(self):
        #__atoms_table = AtomsTable()
        #self.split_to__elements()
        return

    # --------- 供外部调用的获取本物质信息的方法 --------------
    # 获取构成本物质的所有原子字典
    def get_elements(self):

        if not self.__elements:
            tool = SplitToElements(self.formula)
            self.__elements = tool.get_elements()

        return self.__elements

    # 获取本物质的分子量
    def get_mass(self):

        rtn_mass = 0.0

        # 仅当未计算过分子量时采取计算
        if self.__mass > 0:
            rtn_mass = self.__mass
        else:
            # 仅当未分解过原子字典时才去分解
            if not self.__elements:
                self.__elements = self.get_elements()
            # 准备元素周期表
            atoms_table = AtomsTable()  # 内部计算用的 元素
            # 遍历字典，逐个累加分子量
            for key, value in self.__elements.items():
                atom = atoms_table.get_atom_by_symbol(key)
                rtn_mass += atom.mass * value

        return rtn_mass

    # 获取本物质的当前价格
    def get_price(self):
        self._price = random.random() * 10000.00
        return self._price

    # ---------- 本类自行向外输出的方法 ---------------
    # 定义类的自我概况展示
    def show_myself(self):
        print("---------物质概要介绍----------")
        print("中文名称为(%s)，别名[%s]， 化学分子式为(%s)，化学分子量为(%.2f)"  \
              % (self.name, self.alias, self.formula, self.get_mass()))

        print("本物质的元素构成是：")
        print(self.get_elements())

        print("当前价格为：%.2f 元/吨" % (self.get_price()))
        return

