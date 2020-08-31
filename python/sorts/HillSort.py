# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/30 15:47
@Auth ： GavinYang
@File ： HillSort.py   
@IDE ：PyCharm
@Motto： 多反思是否还有更好的实现方式
    希尔排序
"""

import math

'''
    希尔排序是基于插入排序而来的,再此基础上是有提升的.
'''
def hill_sort(nums):
    gap = 1
    while(gap < len(nums) / 3):
        gap = gap * 3 + 1
    while gap > 0:
        print(gap)
        for i in range(gap,len(nums)):
            temp = nums[i]
            # 使用 i 减去 gap , 也就是比如 i 是 6 , gap 是 4的话 ,那么 j 对应的下标是 2
            j = i - gap
            # 如果 j 对应的下标是比 temp,也就是i还要大的话,那么 从 j + gap 的下标都开始往后移动(这里是不是就有点类似插入排序,只是移动的个数不同)
            while j >= 0 and nums[j] > temp:
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = temp    
        gap = math.floor(gap/3)
    return nums    

if __name__ == "__main__":
    nums = [3,2,90,43,24,56,78,34,23,45]        
    nums = hill_sort(nums)
    print(nums)