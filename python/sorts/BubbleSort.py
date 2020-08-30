# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/30 15:47
@Auth ： GavinYang
@File ：BubbleSort.py
@IDE ：PyCharm
@Motto： 多反思是否还有更好的实现方式
    冒泡排序
"""

'''
    进行排序
'''
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]

'''
    进行迭代排序
'''
def bubble_sort_demo(nums):
    for i in range(1,len(nums)):
        for j in range(0,len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    


if __name__ == "__main__":
    nums = [9,3,4,5,1]
    bubble_sort(nums)
    print(nums)