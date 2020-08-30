# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/30 15:47
@Auth ： GavinYang
@File ： ChooesSort.py     
@IDE ：PyCharm
@Motto： 多反思是否还有更好的实现方式
    计数排序
"""  

'''
    计数排序
'''
def count_sort(nums,maxValue):
    bucketLen = maxValue + 1
    bucket = [0] * bucketLen
    sortIndex = 0
    arrlen = len(nums)
    
    # 这里统计下标的个数,比如下标1对应的值是3,那么就说明这个1下标是有三个,也就是对应的值就是出现的个数
    for i in range(arrlen):
        if not bucket[nums[i]]:
            bucket[nums[i]] = 0
        bucket[nums[i]] += 1

    for j in range(bucketLen):
        while bucket[j] > 0:
            nums[sortIndex] = j
            sortIndex += 1
            # 然后这里对个数进行迭代操作
            bucket[j] -= 1
    return nums


    