"""
    预测赢家
"""

'''
    错误的Coding记录
    想法还是太简单了
    使用递归或者dp来实现
'''
def predictWinner(nums):
    count_one = 0
    count_two = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            count_one += nums[i]
        else:
            if i == len(nums) or i == len(nums) - 1:
                continue
            count_two += nums[i]    
    return count_one >= count_two


def recursivePredictTheWinner(nums):
    def total(start,end,turn):
        if start == end:
            return nums[start] * turn
        socreStart = nums[start] * turn + total(start+1,end,-turn)
        socreEnd = nums[end] * turn + total(start,end-1,-turn)
        return max(socreStart * turn , socreEnd * turn) * turn    
    return total(0,len(nums) - 1,1) >= 0

def selfRecusiveTheWinner(nums):

    def record_compare_numer(i,j):
        if(i == j):
            return nums[i]
        pickI = nums[i] -  record_compare_numer(i+1,j)
        pickJ = nums[j] - record_compare_numer(i,j-1)   
        return max(pickI,pickJ)

    return record_compare_numer(0,len(nums) -1 ) >= 0

def dpPredictTheWinner(nums):
    length = len(nums)
    dp = [[0] * length for _ in range(length)]
    for i,num in enumerate(nums):
        dp[i][i] = num
    for i in range(length -2 , -1 , -1):
        for j in range(i + 1, length):
            dp[i][j] = max(nums[i] - dp[i+1][j],nums[j] - dp[i][j-1])    
    return dp[0][length-1] >= 0

if __name__ == "__main__":
    nums = [1,2]
    isFlag = predictWinner(nums)    
    print(isFlag)