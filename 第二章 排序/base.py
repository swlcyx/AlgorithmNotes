# -*- coding: UTF-8 -*-
'''
@Project     ：demo 
@File        ：base.py
@IDE         ：PyCharm 
-------------------------------------
@Author      ：Coisin
@Description ：
@Date        ：2025-02-18 11:42 
-------------------------------------
'''


class SortBase(object):
    """
    排序算法基类
    """

    @classmethod
    def less(cls, a, b) -> bool:
        """
        比较大小
        :param a:
        :param b:
        :return: True | False
        """
        return a < b

    @classmethod
    def exch(cls, a: list, index_1: int, index_2: int) -> None:
        """
        交换数字两元素位置
        :param a:
        :param index_1: 元素1索引
        :param index_2: 元素2索引
        :return:
        """
        a[index_1], a[index_2] = a[index_2], a[index_1]

    @classmethod
    def isSorted(cls, a: list) -> bool:
        """
        判断是否成功排序
        :param a: 数组
        :return:
        """
        if len(a) < 2:
            return True
        for index in range(len(a) - 1):
            if not cls.less(a[index], a[index + 1]):
                return False
            return True
