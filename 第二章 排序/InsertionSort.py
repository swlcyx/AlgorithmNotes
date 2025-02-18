# -*- coding: UTF-8 -*-
'''
@Project     ：demo 
@File        ：InsertionSort.py
@IDE         ：PyCharm 
-------------------------------------
@Author      ：Coisin
@QQ          ：2849068933
@PHONE       ：17350199092
@Description ：
@Date        ：2025-02-18 14:22 
-------------------------------------
'''
from base import SortBase


class Insertion(SortBase):
    @classmethod
    def sort_fn(cls, a: list) -> list:
        n = len(a)
        for index in range(1, n):
            j = index
            while j > 0 and cls.less(a[j], a[j - 1]):
                cls.exch(a, j, j - 1)
                j -= 1
        return a


if __name__ == '__main__':
    a = [2, 32, 242, 54, 5, 3, 25, 6, 7, 31, 4, 556, 89]
    sort_a = Insertion.sort_fn(a)
    print(sort_a)
    print(Insertion.isSorted(a))
