# -*- coding: UTF-8 -*-

# Filename : try_picker.py
# author by : （学员ID)

# 目的：
#       复习使用调用其他类
#       开始简化内部变量名称
#       初步了解 None

import sys
import io


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

print("\n----华丽分割线1--：开始挑选.....")
picked_formula_list = ['Ag', 'AgCl', 'AgNO3', 'Al', 'Al(OH)3', 'Al2(SO4)3', 'Al2O3', 'Al2O3', 'AlCl3', 'Ar']
print("假设已经有了(%d)个物质已经被挑选掉" % (len(picked_formula_list)))

picker = Picker()

# 通过分子式方式，使用挑选机随机挑选1个
print("\n----华丽分割线2--：只挑选一个：")
f_new_pick = picker.pick_one(picked_formula_list)

# 通过分子式方式，使用挑选机继续挑选 n 个
times = 5
print("\n----华丽分割线3--：使用挑选机继续挑选 (%d) 次 ---" % (times))
for i in range(times):
    f_new_pick = picker.pick_one(picked_formula_list)
    print("第(%d)次挑选结果：%s" % (i, f_new_pick))

# 练习二: 通过分子式查找物质的类
print("\n----华丽分割线4--")
mt = MattersTable()
m_picked = mt.get_matter_by_formula('Ag')
m_picked.show_myself()

# 练习三：通过分子式获取物质的原子构成（包括数量）
print("\n----华丽分割线5--")
f_to_find = 'H2O'
m_picked = mt.get_matter_by_formula(f_to_find)
print("本物质(%s)由以下内容构成：" % (f_to_find), end='')
print(m_picked.get_elements())

# 练习四：通过一个 matter 类来使用挑选机
# m = Matter()
print("\n----华丽分割线6--")
m_already_done = []
m_picked = picker.pick_one_matter(m_already_done)
print("本物质 %s 中文名称(%s), 别名(%s)，构成为：" \
      % (m_picked.formula, m_picked.name, m_picked.alias), end='')
print(m_picked.get_elements())

# 练习五：使用挑选机来选取一组 matter
# 确定挑选次数
times = 3
# 准备物质表（物质清单）
#mt = MattersTable()
# 已挑选物质存放的列表
m_already_done = []

# 开始挑选
print("\n----华丽分割线7--：使用挑选机随机挑选 (%d) 次并找出对应的物质 ---" % (times))
for i in range(times):
    # 挑选一次
    m_picked = picker.pick_one_matter(m_already_done)
    print("第(%d)次挑选结果是 %s：" % (i+1, m_picked.formula))
    # m_picked.show_myself()

    # 列出该物质的原子组成
    print("本物质 %s 中文名称(%s), 别名(%s)，构成为：" \
          % (m_picked.formula, m_picked.name, m_picked.alias), end='')
    print(m_picked.get_elements())

# 显示已被挑选的物质
print("总计挑选了 (%d) 个物质，分别是：" % (len(m_already_done)))
for m in m_already_done:
    print(" %s" % (m.formula))

"""
# 练习五： 将练习四包装为 picker 的一个方法，可以挑选出任意个 matter，返回matter 列表
# 输入初始条件：已被挑选的物质分子式列表+定义挑选次数
#picked_formula_list = ['Ag', 'AgCl', 'AgNO3', 'Al', 'Al(OH)3', 'Al2(SO4)3', 'Al2O3', 'Al2O3', 'AlCl3', 'Ar']
picked_formula_list =[]
times = 3

# 调用 picker 类方法进行多次挑选
picked_matter_list = picker.pick_many(picked_formula_list, times)

# 打印挑选结果
print("\n----华丽分割线--：挑选机随机挑选 (%d) 次物质 ---" % (times))
for m in picked_matter_list:
    print("被挑选的物质 %s 中文名称(%s), 别名(%s)，构成为：" \
          % (m.formula, m.name, m.alias), end='')
    print(m.get_elements())
"""




