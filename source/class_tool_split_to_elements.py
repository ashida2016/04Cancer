# -*- coding: UTF-8 -*-

# Filename : class_tool_split_to_elements._elements.py
# author by : （Teacher Mike.Shi)

# 要点：
#       掌握本类的使用方法即可，内容不必理解

class SplitToElements:

    _f = ''                 # 内部使用的分子式
    _elements = {}          #

    # 初始化
    def __init__(self, formula):

        self._f = formula
        self._elements = {}

        # 将分子式第一次拆解： 分离水合物表达式
        e1 = self._split1()

        # 将剩余分子式第二次拆解： 分离某类根 - 分离()部分
        e2 = self._split2()

        # 将剩余的分子式第三次拆解： 分离出剩余元素
        e3 = self._split3()

        # 合并所有的元素集合，并汇总原子个数
        for key, value in e1.items():
            if key in self._elements:
                n = self._elements[key]
                self._elements.update({key: n + value})
            else:
                self._elements.update({key: value})

        for key, value in e2.items():
            if key in self._elements:
                n = self._elements[key]
                self._elements.update({key: n + value})
            else:
                self._elements.update({key: value})

        for key, value in e3.items():
            if key in self._elements:
                n = self._elements[key]
                self._elements.update({key: n + value})
            else:
                self._elements.update({key: value})

        return

    # 获取分拆结果
    def get_elements(self):
        return self._elements


    # 将分子式第一次拆解： 分离水合物表达式
    def _split1(self):
        elements = {}
        num_h2o = 0

        # 前提条件： 水合物表述都在分子式最后，以 •nH2O 形式存在
        try:
            p1 = self._f.index('•')
        except ValueError:
            p1 = 0  # 没有找到水合物特征

        if p1 > 0:
            #
            self._has_hydrate = True

            # 获取水合物表述
            p2 = len(self._f)
            s = self._f[p1+1:p2]

            # 获取 H2O 的位置
            p3 = s.index('H2O')

            # 判断有几个水分子
            # str = s[0:p3]
            if p3 >0 :
                num_h2o = int(s[0:p3])
            else:
                num_h2o = 1

            elements = {'H': 2*num_h2o, 'O': num_h2o}

        return elements

    # 将剩余分子式第二次拆解： 分离某类根 - 分离()部分
    def _split2(self):

        elements = {}
        num_root = 0
        f_root = ''

        # 前提条件： 某类根以 ()n 形式存在，且仅有一个（初中化学）
        # 获取根的表达式
        try:
            p1 = self._f.index('(')
            p2 = self._f.index(')')
            f_root = self._f[p1+1:p2]
        except ValueError:
            p1 = -1     # 没有找到根的特征


        if p1 >= 0:
            # 获取根的数量
            str = self._f[p2+1:len(self._f)]
            p3 = 0  # 至少有1个
            for s in str:
                if s.isdigit():
                    p3 += 1
                else:
                    break
            if p3 > 0:
                num_root = int(str[0:p3])
            else:
                num_root = 1    # 至少有了一个根

            # 将根转换为原子字典
            elements = self._split_nomal(f_root)
            # 将所有的原子数量都乘以根的数量
            for key,value in elements.items():
                value = value * num_root
                elements.update({key: value})

        return elements

    # 将剩余的分子式第三次拆解： 分离出剩余元素
    def _split3(self):

        remainder1 = self._f
        remainder2 = ''
        remainder3 = ''

        # 先去除水合物表达式
        # 前提条件： 水合物表述都在分子式最后，以 •nH2O 形式存在
        try:
            p1 = self._f.index('•')
        except ValueError:
            p1 = 0  # 没有找到水合物特征

        if p1 > 0:
            remainder1 = self._f[:p1]

        # 再去除根的表达式
        try:
            p1 = remainder1.index('(')
            p2 = remainder1.index(')')
        except ValueError:
            p1 = -1     # 没有找到根的特征

        if p1 >= 0:

            # 先取出 ( 左边的表达式
            if p1 > 0:
                remainder2 = remainder1[:p1]

            # 判断 ) 右边是否有2个数字 - ) 前提条件： ）右边至少有一个数字
            n = len(remainder1)
            if p2 < len(remainder1) - 2:
                c2 = remainder1[p2+2]
                if c2.isdigit():
                    p2 += 3
                else:
                    p2 += 2
            else:
                p2 += 1

            # 取出右边的表达式
            if p2 == len(remainder1) - 1:
                remainder3 = ''
            else:
                remainder3 = remainder1[p2:]

            # 若找到根表达式，则使用去除根后的两部分
            remainder = remainder2 + remainder3
        else:
            remainder = remainder1      # 若没有找到根的部分，则直接使用去除水合物表达式部分的剩余量

        # 将剩余部分转换为原子字典
        elements = self._split_nomal(remainder)

        return elements

    # 将不含某类根或水合物的普通分子式拆分为原子字典
    def _split_nomal(self, formula):

        elements = {}

        pstart = 0
        pend = len(formula) - 1

        while pstart <= pend:


            if pstart == pend:
                # 最后一位情况直接处理
                atom_name = formula[pstart]
                atom_num = 1
            else:
                # 从已处理完毕的字符串向后找，去除已处理部分
                sub = formula[pstart:]
                # 原子名称和数量清零
                atom_name = ''
                atom_num = 0

                # 获取原子符号 前提条件：1-2位， 单个大写字母或一大一小2个字母
                if pstart < pend:
                    c = sub[1]
                    if c.islower():
                        # 当其后一位为小写字母时，原子符号为双字母
                        atom_name = sub[0] + sub[1]
                    else:
                        # 其余情况均为单字母
                        atom_name = sub[0]
                else:
                    # 截取到最后一位时
                    atom_name = sub[0]

                # 获取原子的数量 前提条件： 原子数量为1-2位数字
                # c1, c2 为检查后两位是否为数字的字符
                p1 = sub.index(atom_name) + len(atom_name)
                if p1 < len(sub):
                    c1 = sub[p1]
                    if c1.isdigit():
                        if p1 < len(sub) - 1:
                            c2 = sub[p1+1]
                            if c2.isdigit():
                                atom_num = int(c1+c2)
                            else:
                                atom_num = int(c1)
                        else:
                            atom_num = int(c1)
                    else:
                        atom_num = 1
                else:
                    atom_num = 1

            # 查找是当前找到的原子是否已经在字典内
            if atom_name in elements:
                # 如果存在要将值取出后，与当前原子数累加再存入
                n = elements[atom_name]
                elements.update({atom_name: atom_num + n})
            else:
                elements.update({atom_name: atom_num})

            # 当原子个数为 1 时，字符串指针不调整
            if atom_num == 1:
                pstart += len(atom_name)
            else:
                pstart += len(atom_name) + len(str(atom_num))

        return elements
