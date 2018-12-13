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


# 练习三：组合 2 种物质， 计算他们的原子总量
picker = Picker()
#picked_f_list


