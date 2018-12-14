# -*- coding: UTF-8 -*-

# Filename : class_matters_table.py
# author by : （学员ID)

# 目的： 学会建立类的列表
#       加深类的使用方法
#       加深理解函数返回值的使用
# 配套练习：
#       try_class4.py

import os
"""
import sys
import io
"""
import pandas as pd
import numpy as np

# 引用物质类
from class_matter import Matter

class MattersTable:

    # 私有属性
    _matters = []         # 所有物质对象的 list
    _count = 0          # 本表容纳的物质种类数
    _max_mass = 0.0
    _min_mass = 0.0

    # 公共属性
    table_ver = ""
    matters_iterator = iter(_matters)

    # 创建 matters 列表
    # 定义构造方法
    def __init__(self):
        # 原子表名称
        table_ver = "物质种类表 Ver1.0 "

        # 将 CSV 文件内容读入内存
        # 设定 CSV 文件所在的路径 path （注意在 ATOM 和 CMD 环境下当前工作路径有所差异）
        # for ATOM
        # csv_path = os.getcwd() + '\\' + 'config\\all_matters.csv'
        # for cmd Python
        # csv_path = os.getcwd() + '\\' + '..\\config\\all_matters.csv'
        # for PyCharm
        csv_path = '..\\config\\all_matters.csv'
        # print(csv_path)
        df = pd.read_csv(csv_path, sep=',')
        # 将CSV内容转化为二维数组
        data = np.array(df.loc[:, :])

        _matters = []
        # 顺序读取所有元素，并初始化每个实例化的类
        for row in data:
            # 新生成一个空白的物质类
            matter = Matter()
            # 读取每一行的原子信息，并存入相应的类属性
            matter.name = row[0]
            matter.alias = row[1]
            matter.formula = row[2]
            matter.catalog1 = (row[3])
            matter.comment = row[4]
            # 自动拆分物质的分子式
            f = matter.get_elements()
            # 自动计算物质的分子量
            n = matter.get_mass()
            # 自动获取物质的价格
            p = matter.get_price()

            # 将填好信息的原子类加入列表
            self._matters.append(matter)

        # 更新计数器
        self._count = len(self._matters)
        # 更新最大最小值
        # self._refresh_maxmin()

        return

    def get_matter_by_formula(self, f):

        found_matter = Matter()

        # 遍历搜寻
        for m in self._matters:
            if m.formula == f:
                found_matter.name       = m.name
                found_matter.alias      = m.alias
                found_matter.formula    = f
                found_matter.catalog1   = m.catalog1
                found_matter.comment    = m.comment

        return found_matter

