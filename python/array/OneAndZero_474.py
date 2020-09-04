"""
    一和零
    leetCode: https://leetcode-cn.com/problems/ones-and-zeroes/
"""

'''
    Strs是字符串集合
    m: 0的个数
    n: 1的个数
'''
def findMaxForm(strs,m,n):
    if(len(strs) == 0 or (m == 0 and n ==0)):
        return 0
    return tryFindMaxForm(strs,len(strs)-1,m,n)

def tryFindMaxForm(strs,i,m,n):
    if(i < 0):
        return 0
    numZero = 0
    numOne = 0
    strValue = strs[i]
    for j in range(len(strValue)):
        if(strValue[j] == '0'):
            numZero += 1
        else:
            numOne += 1
    if(m >= numZero and n >= numOne):
        return max(tryFindMaxForm(strs,i-1,m,n),1+tryFindMaxForm(strs,i-1,m-numZero,n-numOne))
    else:
        return tryFindMaxForm(strs,i-1,m,n)                


if __name__ == "__main__":
    strs = ["10","0001","11101","1","0"]
    m = 5
    n = 3
    print(findMaxForm(strs,m,n))       