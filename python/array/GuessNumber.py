# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/30 0:57
@Auth ： GavinYang
@File ：GuessNumber.py
@IDE ：PyCharm
@Motto： 多反思是否还有更好的实现方式
猜数字游戏
leetCode: https://leetcode-cn.com/problems/guess-numbers/
"""

def guestNumberGame(guess,answer):
    correct_count = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            correct_count += 1
    return correct_count
    #pass

if __name__ == '__main__':
    guess = [1,2,3]
    answer = [1,2,3]
    correct_count = guestNumberGame(guess,answer)
    print(correct_count)