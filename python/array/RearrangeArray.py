'''
    重新排列数组
    难度: 简单
    date: 2020-08-28
    leetcode url : https://leetcode-cn.com/problems/shuffle-the-array/
'''

'''
    思路,当利用下标获取出x1的值的时候,也可以获取出y1的值,也就是只用迭代一半数据的意思
    
'''
def shuffle(nums,n):
    numList = []
    for i in range(0,n):
        numList.append(nums[i])
        numList.append(nums[i + n])
    return numList

if __name__ == "__main__":
    nums = [1,1,2,2]
    n = 2
    numsList = shuffle(nums,n)    
    print(numsList)