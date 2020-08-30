# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/30 15:47
@Auth ： GavinYang
@File ： MergeSort.py
@IDE ：PyCharm
@Motto： 多反思是否还有更好的实现方式
    归并排序
"""

import math

'''
    使用递归调用 merge_sort 方法,使用递归需要注意的是返回值问题,否则就会由死递归啦....
    对左右数组,一直进行分,一直分到其长度是小于2的,然后再进行比较,最后合并比较.
'''
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    middle = math.floor(len(nums)/2)
    left,right = nums[0:middle],nums[middle:]
    # 递归调用 merge_sort 方法就是继续往下细分比较.
    return merger_two_number(merge_sort(left),merge_sort(right))

def merger_two_number(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))  
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))                
    return result

if __name__ == "__main__":
    nums = [45,3,43,78,4,34]
    nums = merge_sort(nums)    
    print(nums)