"""
    一维数组动态和
"""

'''
    维持一个当前i之前的总和值参数.
'''
def runningSum(nums):
    if len(nums) > 0:
        record_value = nums[0]
        for i in range(1,len(nums)):
            temp = nums[i]
            nums[i] = record_value + nums[i]
            record_value += temp

'''
    使用一个存储相加完后的数组保存数据,然后从原始的拿上一个.
'''
def copyRunningSum(nums):
    copyNums = nums
    for i in range(1,len(nums)):
        copyNums[i] = copyNums[i-1] + nums[i]
    return copyNums

if __name__ == "__main__":
    nums = [3,1,2,10,1]
    nums = copyRunningSum(nums)
    print(nums)            
