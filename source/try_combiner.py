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
import operator

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
chemical_equation = cmb.make_formula_of2(a, m1, b, m2)
print("反应式： %s " % (chemical_equation))
# 列出反应物的原子种类与数量
after_reaction = cmb.mix2(a, m1, b, m2)
print("反应后的原子字典为：", end='')
print(after_reaction)

# 练习四：从物质表中随意选取 2 种不同物质各n份，假设它们无论如何配比都能起反应，求每次反应后的原子种类及数量
print("---练习四---")
# 清空已挑选物质列表
m_already_done =[]

# 随机挑选 2 个不同物质
m1 = picker.pick_one_matter(m_already_done)
m2 = picker.pick_one_matter(m_already_done)

# 确定物质份数并开始循环
a_max = 2
b_max = 2
count = 1
for a in range(0, a_max + 1):
    for b in range(0, b_max + 1):
        # 自动生成化学反应式
        chemical_equation = cmb.make_formula_of2(a, m1, b, m2)

        # 选取份数可以从0开始，但如果两种都为0，则跳过
        if chemical_equation:
            # 列出反应物的原子种类与数量
            before_reaction = cmb.mix2(a, m1, b, m2)

            # 打印输出
            print("反应式(%d)：%s  --> " % (count, chemical_equation), end='')
            print(before_reaction)

            # 计数器
            count += 1

# 练习五：从物质表中随意选取 2个不重复的物质，列举所有可能的组合
print("---练习五---")

# 生成一张物质表
count_ij = 0
mt = MattersTable()
for i in range(mt._count):
    for j in range(i + 1, mt._count):

        # 计数器
        count_ij += 1

        # 循环输出所有组合
        m1 = Matter()
        m1 = mt._matters[i]

        m2 = Matter()
        m2 = mt._matters[j]
        #print("No.%d %s + %s" %(count_ij, m1.formula, m2.formula))

# 练习六：从物质表中随意选取 2个不重复的物质，每种最多可以配 n 份，列举所有可能的组合
print("---练习六---")
# 生成一张物质表
count_ij = 0
mt = MattersTable()
for i in range(mt._count):
    for j in range(i + 1, mt._count):

        # 计数器
        count_ij += 1

        # 循环输出所有组合
        m1 = Matter()
        m1 = mt._matters[i]

        m2 = Matter()
        m2 = mt._matters[j]
        # print("No.%d %s + %s" %(count_ij, m1.formula, m2.formula))

        # 确定物质份数并开始循环
        a_max = 2
        b_max = 3
        count_ab = 1
        for a in range(0, a_max + 1):
            for b in range(0, b_max + 1):
                # 自动生成化学反应式
                s = cmb.make_formula_of2(a, m1, b, m2)

                if s:
                    # 列出反应物的原子种类与数量
                    reaction_formula = cmb.mix2(a, m1, b, m2)

                    # 打印输出
                    #print("反应式(%d - %d)：%s  --> " % (count_ij, count_ab, s), end='')
                    #print(reaction_formula)

                    # 计数器
                    count_ab += 1

# 练习七: 将练习四与练习六合并 =》 暴力配平方程式
print("---练习七---")
print("开始寻找.....")
# 清空已挑选物质列表
m_already_done =[]

# 随机挑选 2 个不同物质
m1 = picker.pick_one_matter(m_already_done)
m2 = picker.pick_one_matter(m_already_done)

# 确定物质份数并开始循环
a_max = 10
b_max = 10
mt = MattersTable()

count_found = 0
count_ab = 0
for a in range(0, a_max + 1):
    for b in range(0, b_max + 1):

        count_ab += 1

        # 第一步，对反应物按不同的份数进行组合 (before)
        # 自动生成化学反应式
        before_equation = cmb.make_formula_of2(a, m1, b, m2)
        if before_equation:
            # 列出反应物的原子种类与数量
            before_reaction = cmb.mix2(a, m1, b, m2)

            # 第二步，2种物质，n种份数的所有组合 (after)
            # 生成一张物质表
            count_ij = 0
            for i in range(mt._count):
                for j in range(i + 1, mt._count):

                    # 计数器
                    count_ij += 1

                    # 循环输出所有组合（单个）
                    m3 = Matter()
                    m3 = mt._matters[i]

                    m4 = Matter()
                    m4 = mt._matters[j]
                    # print("No.%d %s + %s" %(count_ij, m3.formula, m4.formula))

                    # 确定物质份数并开始循环
                    c_max = 10
                    d_max = 10
                    count_cd = 0
                    for c in range(0, c_max + 1):
                        for d in range(0, d_max + 1):
                            # 计数器
                            count_cd += 1

                            # 自动生成化学反应式
                            after_equation = cmb.make_formula_of2(c, m3, d, m4)
                            if after_equation:
                                # 列出反应物的原子种类与数量
                                after_reaction = cmb.mix2(c, m3, d, m4)

                                # 第三步：比较反应前后的原子种类与数量，如果完全相同则认为反应成立
                                if operator.eq(before_reaction, after_reaction) == True:
                                    if m1.formula == m3.formula or m1.formula == m4.formula:
                                        pass
                                    else:
                                        if m2.formula == m3.formula or m2.formula == m4.formula:
                                            pass
                                        else:
                                            count_found += 1
                                            # 打印输出
                                            print("*****终于找到第 (%d) 个成立的反应式*****" % (count_found))
                                            print("反应式(%d-%d-%d)：%s  --> %s " % \
                                                 (count_ab, count_ij, count_cd, before_equation, after_equation))
                                            print("  反应前原子种类与数量：", end='')
                                            print(before_reaction)
                                            print("  反应后原子种类与数量：", end='')
                                            print(after_reaction)

print("总共找到 (%d) 对成立的反应式" % (count_found))

