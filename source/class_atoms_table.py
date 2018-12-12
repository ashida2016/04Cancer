# -*- coding: UTF-8 -*-

# Filename : class_atoms_table.py
# author by : （学员ID)

# 目的： 加深学习类的使用方法（类定义中使用其他类）
#       理解为外部调用类而创造的公用方法
#       加深理解函数返回值的使用
#       了解 iteraror 的用法
# 配套练习：
#       try_class2.py

import os
import sys
import io

import pandas as pd
import numpy as np

# 读取原子类
from class_atom import Atom

# 类定义
class AtomsTable:

    # 私有属性
    _atoms = []         # 所有元素对象的 list
    _count = 0          # 本表容纳的原子个数
    _max_seq = 0      # 最大的原子序号
    _min_seq = 0      # 最小的原子序号
    _max_mass = 0.0
    _min_mass = 0.0

    # 公共属性
    table_ver = ""
    atoms_iterator = iter(_atoms)

    # 创建 atoms 列表
    # 定义构造方法
    def __init__(self):
        # 原子表名称
        table_ver = "元素周期表 Ver1.0 "

        # 将 CSV 文件内容读入内存
        # 设定 CSV 文件所在的路径 path （注意在 ATOM 和 CMD 环境下当前工作路径有所差异）
        # for ATOM
        # csv_path = os.getcwd() + '\\' + 'config\\all_atoms.csv'
        # for cmd Python
        # csv_path = os.getcwd() + '\\' + '..\\config\\all_atoms.csv'
        # for PyCharm
        csv_path = '..\\config\\all_atoms.csv'
        df = pd.read_csv(csv_path, sep=',')
        # 将CSV内容转化为二维数组
        data = np.array(df.loc[:, :])

        # 顺序读取所有元素，并初始化每个实例化的类
        for row in data:
            # 新生成一个空白的原子类
            self._atom = Atom()
            # 读取每一行的原子信息，并存入相应的类属性
            self._atom.seq = row[0]
            self._atom.symbol = row[1]
            self._atom.name = row[2]
            self._atom.set_spell_zh(row[3])
            self._atom.mass = row[4]
            self._atom.set_name_en(row[5])
            self._atom.period = row[6]
            self._atom.family = row[7]
            self._atom.catalog = row[8]
            # 将填好信息的原子类加入列表
            self._atoms.append(self._atom)

        # 更新计数器
        self._count = len(self._atoms)
        # 更新最大最小值
        self._refresh_maxmin()

        return

    # 遍历所有元素，更新最大&最小 原子序数及相对质量
    def _refresh_maxmin(self):
        # 建立比较基准
        max_seq = -1
        max_mass = -1
        min_seq = 9999
        min_mass = 9999

        # 遍历，寻找最大最小值
        for atom in self._atoms:
            if atom.seq > max_seq:
                max_seq = atom.seq
            if atom.seq < min_seq:
                min_seq = atom.seq
            if atom.mass > max_mass:
                max_mass = atom.mass
            if atom.mass < min_mass:
                min_mass = atom.mass

        # 更新内部属性
        self._max_seq = max_seq
        self._min_seq = min_seq

        self._max_mass = max_mass
        self._min_mass = min_mass

        return


    # ---------- 以下为供外部调用的函数 --------------
    # 获取原子列表的个数
    def get_count(self):
        return self._count

    # 获取最大最小值 - 原子序号
    def get_max_seq(self):
        return self._max_seq

    def get_min_seq(self):
        return self._min_seq

    # 获取最大最小值 - 相对原子量
    def get_max_mass(self):
        return self._max_mass

    def get_min_mass(self):
        return self._min_mass

    # 依据指定的原子序号获取的原子信息（返回一个 atom 类）
    def get_atom_by_seq(self, num):
        found_atom = Atom()
        # 遍历搜寻
        for atom in self._atoms:
            if atom.seq == num:
                found_atom.seq      = atom.seq
                found_atom.symbol   = atom.symbol
                found_atom.name     = atom.name
                found_atom.set_spell_zh(atom.get_spell_zh())
                found_atom.mass     = atom.mass
                found_atom.set_name_en(atom.get_name_en())
                found_atom.period   = atom.period
                found_atom.family   = atom.family
                found_atom.catalog  = atom.catalog

        return found_atom

    # 依据指定的原子英文符号获取的原子信息（返回一个 atom 类）
    def get_atom_by_symbol(self, symbol):
        found_atom = Atom()
        # 遍历搜寻
        for atom in self._atoms:
            if atom.symbol == symbol:
                found_atom.seq      = atom.seq
                found_atom.symbol   = atom.symbol
                found_atom.name     = atom.name
                found_atom.set_spell_zh(atom.get_spell_zh())
                found_atom.mass     = atom.mass
                found_atom.set_name_en(atom.get_name_en())
                found_atom.period   = atom.period
                found_atom.family   = atom.family
                found_atom.catalog  = atom.catalog

        return found_atom
