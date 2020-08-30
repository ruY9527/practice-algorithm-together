# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/30 15:47
@Auth ： GavinYang
@File ：InsertSort.py
@IDE ：PyCharm
@Motto： 多反思是否还有更好的实现方式
    插入排序
"""

'''
    个人误区:  由于常规的for循环,习惯数据从最初的前面开始往后面移动,
              这里应该是由最后的一位往后面移动,并且数据也一直往后面移动即可.
               然后记录的值,就插入到移动的完了后最前面的那个index卡槽里面去.
    ~~~~~  真是菜的我啊              
'''
def insert_sort(nums):
    for i in range(len(nums)):
        preIndex = i -1
        current = nums[i]
        while preIndex >= 0 and nums[preIndex] > current:
            nums[preIndex + 1] = nums[preIndex]
            preIndex -= 1
        nums[preIndex+1] = current

        

if __name__ == "__main__":
    nums = [2,5,3,79,48,50]
    insert_sort(nums)
    print(nums)