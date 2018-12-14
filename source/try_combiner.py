# -*- coding: UTF-8 -*-

# Filename : try_combiner.py
# author by : （学员ID)

# 目的：
#       复习使用调用其他类
#       开始简化内部变量名称
#       学习暴力组合法的基本技巧

import sys
import io

import pandas as pd
import numpy as np

# 引用元素周期表类
from class_atoms_table import AtomsTable

# 引用物质类
from class_matter import Matter

# 引用物质表类
from class_matters_table import MattersTable

# 引用挑选机类
from class_picker import Picker

# 引用组合机类
from class_combiner import Combiner


# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 练习一： 用双重循环组合2个列表
a = ['a', 'b']
b = ['0', '1']
for i in range(2):
    for j in range(2):
        result = a[i] + b[j]
        print(result)

# 练习二： 用三重循环组合3个列表
a = ['A', 'B']
b = ['x', 'y', 'z']
c = ['0', '1', '2', '4']

count = 0
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            result = a[i] + b[j] + c[k]
            count += 1
            print("第(%d)次组合：%s" % (count, result))


# 练习三：随意组合指定份数的 2 种不同物质，假设其能起反应，求出其反应后的原子种类及数量
print("---练习三---")
# 准备挑选机
picker = Picker()
# 已挑选物质存放的列表
m_already_done = []

# 手工挑选2个物质， 并指定数量， 让其混合后计算所包含的原子种类与数量
a = 10
m1 = picker.pick_one_matter(m_already_done)
b = 10
m2 = picker.pick_one_matter(m_already_done)
# print("挑选了 (%d) 个 %s 和 (%d) 个 %s 进行反应：" % (a, m1.formula, b, m2.formula))

# 开始使用组合机
cmb = Combiner()
# 自动生成化学反应式
s = cmb.make_formula_of2(a, m1, b, m2)
print("反应式： %s " % (s))
# 列出反应物的原子种类与数量
after_reaction = cmb.mix2(a, m1, b, m2)
print("反应后的原子字典为：", end='')
print(after_reaction)

# 练习四：随意组合 2 种不同物质各n份，假设它们无论如何配比都能起反应，求每次反应后的原子种类及数量
print("---练习四---")
m_already_done =[]

a_max = 3
b_max = 3

for a in range(1, a_max + 1):
    for b in range(1, b_max + 1):
        # 随机挑选 2 个不同物质
        m1 = picker.pick_one_matter(m_already_done)
        m2 = picker.pick_one_matter(m_already_done)

        # 自动生成化学反应式
        s = cmb.make_formula_of2(a, m1, b, m2)

        # 列出反应物的原子种类与数量
        after_reaction = cmb.mix2(a, m1, b, m2)

        print("反应式： %s  --> 反应后的原子字典为：" %(s), end='')
        print(after_reaction)

