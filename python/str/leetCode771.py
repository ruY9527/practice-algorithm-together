# -*- coding: utf-8 -*-
"""
    LeetCode: https://leetcode-cn.com/problems/jewels-and-stones/
"""

'''
    使用字典来封装数据
'''
def newJeweIsIntones(j,s):
    char__count = dict()
    for i in range(len(s)):
        simple_char = char__count.get(s[i])
        if simple_char is None:
            simple_char = 1
        else:
            simple_char += 1
        char__count[s[i]] = simple_char
    total = 0
    for i in range(len(j)):
        simple_count = char__count.get(j[i])
        if simple_count is not None:
            total += simple_count
    return total        

'''
    先转化为 set 集合, 然后迭代字符串 S 的时候, 去判断是否有包含,
    如果是有包含的话,那么count就会加一的
'''
def conciseCodingFunction(J,S):
    Jset = set(J)
    return sum(s in Jset for s in S)
    #pass

if __name__ == "__main__":
    j = "z"
    s = "ZZ"
    count = newJeweIsIntones(j,s)   
    print(count)