# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/30 15:47
@Auth ： GavinYang
@File ： ChooesSort.py     
@IDE ：PyCharm
@Motto： 多反思是否还有更好的实现方式
    选择排序
"""

def chooes_sort(nums):
    for i in range(len(nums)):
        min_value = nums[i]
        index_value = i
        for j in range(i,len(nums)):
            if nums[j] < min_value and i != j:
                min_value = nums[j]
                index_value = j
        print(i)
        print(index_value)
        print('------------')        
        nums[i] , nums[index_value] = nums[index_value] , nums[i]

'''
    选择排序,每次选择是最大的或者是最小的
'''
def select_sort(nums):
    for i in range(len(nums)):
        minIndex = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j
        if i != minIndex:
            nums[i],nums[minIndex] = nums[minIndex],nums[i]
    pass


if __name__ == "__main__":
    nums = [9,2,1]
    chooes_sort(nums)
    print(nums)        