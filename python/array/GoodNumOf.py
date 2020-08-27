"""
    好数对题目
    address: https://leetcode-cn.com/problems/number-of-good-pairs/
"""

import collections

'''
    暴力破解法,使用的是二层for循环
    其思路主要是统计次数,可以利用出现的次数:  比如 1 出现了 4 次的话, 那么就可以利用 4 --> 1+2+3(最后统计6)
    也就是利用  v * (v - 1) / 2
'''
def numIdenticalPairs(nums):
    count = 0 
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count            

'''
    利用 Dict字典来进行次数.
    其实这里还有一个便捷情况,可以使用数组来保存,但是数组自身得有一个100个,这样迭代的情况就比使用字典多.
    但是这里比起官方给出来的代码,是啰嗦了不少.
    如果排好序,然后来前后比较,统计个数呢?  貌似也是一种解法,但是比起使用字典来的话,肯定不是最优的
'''
def useCollectorsNums(nums):
    data_dict = dict()
    all_count = 0
    for i in nums:
        data_count = data_dict.get(i)
        if data_count is None:
            data_count = 1
        else:
            data_count += 1
        data_dict[i] = data_count
    for key,value in data_dict.items():
        all_count += value * (value-1) / 2
    return all_count

'''
    基于python3 最新简洁的代码
'''
def useConciseCodePython(nums):
    m = collections.Counter(nums)
    return sum(v * (v-1) // 2 for k,v in m.items())

    
if __name__ == "__main__":
    nums = [1,1,1,1,1]
    count = numIdenticalPairs(nums)
    dict_count = useCollectorsNums(nums)
    print(count)
    print(dict_count)