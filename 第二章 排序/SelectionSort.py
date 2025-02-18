# -*- coding: UTF-8 -*-
'''
@Project     ：demo 
@File        ：selection_sort.py
@IDE         ：PyCharm 
-------------------------------------
@Author      ：Coisin
@QQ          ：2849068933
@PHONE       ：17350199092
@Description ：
@Date        ：2025-02-18 13:57 
-------------------------------------
'''
from base import SortBase


class Selection(SortBase):
    @classmethod
    def sort_fn(cls, a: list) -> list:
        n = len(a)
        for index in range(n):
            min_attr = index
            for idx in range(index + 1, n):
                if cls.less(a[idx], a[min_attr]):
                    min_attr = idx
            if min_attr != index:
                cls.exch(a, index_1=index, index_2=min_attr)
        return a


if __name__ == '__main__':
    a = [2, 32, 242, 54, 5, 3, 25, 6, 7, 31, 4, 556, 89]
    sort_a = Selection.sort_fn(a)
    print(sort_a)
    print(Selection.isSorted(a))
