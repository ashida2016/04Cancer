# -*- coding: UTF-8 -*-

# Filename : class_atom.py
# author by : （学员ID)

# 要点： 类的基本概念
#       掌握将元素周期表上的元素定义转化为类
#       理解构造类的用途
#       掌握类的公有，私有属性概念
#       掌握公有属性，公有属性的调用方法
# 配套练习：
#       try_class1.py

# 类定义
class Atom:

    # 定义类public属性（可公开被外部直接调用）
    seq = 33          # 原子序号
    name = '砷'                 # 元素中文符号
    symbol = 'As'               # 元素英文符号
    mass = 74.92                # 精确的相对原子质量
    period = 4                  # 属于哪个周期（行）
    family = 'V-A'              # 属于哪个族（列）
    catalog = '非金属'           # 属于哪个分类

    # 定义private属性（私有属性在类外部无法直接进行访问)
    # 元素的高级属性
    __name_en = 'Arsenic'
    __spell_zh = 'shēn'

    # 定义构造方法
    def __init__(self):
        self.seq = 0
        self.symbol = 'Unknown'
        self.name = 'Unknown'
        self.mass = 0.0
        self.period = 0
        self.family = 'Unknown'
        self.catalog = 'Unknown'

        self.set_name_en('Unknown')
        self.set_spell_zh('Unknown')
        return

    # -------以下为类的公用方法----------
    # 定义私有属性读取方法
    def set_name_en(self, value):
        self.__name_en = value
        return

    def get_name_en(self):
        value = self.__name_en
        return str(value)

    def set_spell_zh(self, value):
        self.__spell_zh = value
        return

    def get_spell_zh(self):
        value = self.__spell_zh
        return str(value)

    # 定义类的自我展示
    def show_myself(self):
        print("本元素的原子序号为(%d)，中文(%s)[%s]， 英文(%s)[%s]，类型为%s，相对原子量为(%.3f)"  \
              % ( self.seq,                       \
                  self.name, self.get_spell_zh(),   \
                  self.symbol, self.get_name_en(),  \
                  self.catalog, self.mass )       \
              )
        return
