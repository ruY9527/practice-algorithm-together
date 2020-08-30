# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/30 15:47
@Auth ： GavinYang
@File ： QuickSort.py
@IDE ：PyCharm
@Motto： 多反思是否还有更好的实现方式
    快速排序
"""

def quick_sort(nums,left=None,right=None):
    left = 0 if not isinstance(left,(int,float)) else left
    right = 0 if not isinstance(right,(int,float)) else right
    if left < right:
        # 
        partitionIndex = partition(nums,left,right)

        # 分为左右二边数组,然后使用递归调用
        quick_sort(nums,left,partitionIndex - 1)
        quick_sort(nums,partitionIndex + 1, right)
    return nums    

def partition(nums,left,right):
    # 设置 基准值,
    pivot = left
    index = pivot + 1
    i = index
    # 从 left的第二位(+1)开始迭代,
    while i <= right:
        # 如果比 基准值 还要小的话,那么就进行交换
        if nums[i] < nums[pivot]:
            nums[i] , nums[index] = nums[index],nums[i]
            index += 1
        # 跳出循环    
        i += 1
    nums[pivot],nums[index-1] = nums[index-1],nums[pivot]        
    return index -1