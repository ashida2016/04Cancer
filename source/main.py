# -*- coding: UTF-8 -*-

# Filename : main.py
# author by : （学员ID)

# 目的： 初步认识 main.py
#       复习使用调用其他类
#       开始简化内部变量名称

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


# 练习一：随机挑选 n 个不重复的物质
# 示例：假设已经挑选了所有 A 字头的物质
picked_formula_list = ['Ag', 'AgCl', 'AgNO3', 'Al', 'Al(OH)3', 'Al2(SO4)3', 'Al2O3', 'Al2O3', 'AlCl3', 'Ar']
print("假设已经有了(%d)个物质已经被挑选掉" % (len(picked_formula_list)))

print("\n----华丽分割线--：开始挑选.....")
picker = Picker()

# 使用挑选机随机挑选1个
print("\n----华丽分割线--：只挑选一个：")
f_new_pick = picker.pick_one(picked_formula_list)

# 使用挑选机继续挑选 n 个
times = 5
print("\n----华丽分割线--：使用挑选机继续挑选 (%d) 次 ---" % (times))
for i in range(times):
    f_new_pick = picker.pick_one(picked_formula_list)
    print("第(%d)次挑选结果：%s" % (i, f_new_pick))

# 练习二: 通过分子式查找物质的类
print("\n----华丽分割线--")
mt = MattersTable()
m_picked = mt.get_matter_by_formula('Ag')
m_picked.show_myself()

# 练习三：通过分子式获取物质的原子构成（包括数量）
print("\n----华丽分割线--")
f_to_find = 'H2O'
m_picked = mt.get_matter_by_formula(f_to_find)
print("本物质(%s)由以下内容构成：" % (f_to_find), end='')
print(m_picked.get_elements())

# 练习四：组合练习一二三
# 确定挑选次数
times = 10
# 准备物质表（物质清单）
mt = MattersTable()
# 开始挑选
print("\n----华丽分割线--：使用挑选机随机挑选 (%d) 次并找出对应的物质 ---" % (times))
for i in range(times):
    # 挑选一次
    f_new_pick = picker.pick_one(picked_formula_list)
    print("第(%d)次挑选结果是 %s：" % (i+1, f_new_pick))
    # 用挑选出来的分子式去寻找物质
    m_picked = mt.get_matter_by_formula(f_new_pick)
    # m_picked.show_myself()
    # 列出该物质的原子组成
    # e_picked = m_picked.get_elements()
    print("本物质 %s 中文名称(%s), 别名(%s)，构成为：" \
          % (m_picked.formula, m_picked.name, m_picked.alias), end='')
    print(m_picked.get_elements())





