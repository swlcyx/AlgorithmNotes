# -*- coding: UTF-8 -*-
'''
@Project     ：demo 
@File        ：BinarySearch.py
@IDE         ：PyCharm 
-------------------------------------
@Author      ：Coisin
@Description ：
@Date        ：2025-02-18 10:14 
-------------------------------------
'''


def BinarySearch(key: int, a: [int]):
    """
    二分查找
    :param key: 需要查找的值
    :param a: 有序列表
    :return: 目标值索引，不存在则返回-1
    """
    left = 0
    right = len(a) - 1
    while left <= right:
        # 被查找的键要么不存在，要么必然存在于 a[left..right] 之中
        mid = left + (right - left) // 2  # //是整除
        if key < a[mid]:
            right = mid - 1
        elif key > a[mid]:
            left = mid + 1
        else:
            return mid
    return -1


def main():
    filename = "largeText.txt"
    whitelist = list(map(int, open("tinyAllowlist.txt").readlines()))
    whitelist.sort()  # 对数组进行排序
    for key in list(map(int, open("largeAllowlist.txt").readlines())):
        if BinarySearch(key=key, a=whitelist) < 0:
            # 读取键值，如果不存在于白名单中则将其打印
            print(key)


if __name__ == '__main__':
    main()
