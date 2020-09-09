"""
    组合总和 
    leetCode 39
    leetCode: https://leetcode-cn.com/problems/combination-sum/
"""

"""
    use: 表示已经使用过的数(组成的列表) , remain 表示距离target还有多大
    递归求可能的组合. 每次递归时对所有的candidates做一次遍历,情况有3:1. 
"""
def combinationSum(candidates,tag):
    candidates = sorted(candidates)
    ans = []
    
    def find(s,use,remain):
        for i in range(s,len(candidates)):
            c = candidates[i]
            if c == remain:
                ans.append(use + [c])
            if c < remain:
                find(i,use+[c],remain-c)    
            if c > remain:
                return    
    find(0,[],tag)
    return ans