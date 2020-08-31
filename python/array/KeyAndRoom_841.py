"""
    房间和钥匙
    LeetCode841: https://leetcode-cn.com/problems/keys-and-rooms/  
"""

import collections

'''
    本人错误解法,思路还是不够清晰的.
    问题: 如果出现那种刚好没有的在前面的下标,然后对应的下标再后面又有了,就会直接导致出返回False.
'''
def canVisitAllRooms(rooms):
    keySet = []
    keySet.append(0)
    keySet.extend(rooms[0])
    first_no_index = []
    for i in range(1,len(rooms)):
        if len(rooms[i]) == 0:
            continue
        if i not in keySet:
            first_no_index.append(i)
        else:
            keySet.extend(rooms[i])   
    for value in first_no_index:
        if value not in keySet:
            print(value)
            return False 
        else:
            keySet.extend(rooms[value])             
    return True



'''
    深度优先:   vis 中存储进入门的索引,也就是钥匙,没把钥匙都是对应的索引.
                nums 也是进入的次数,  如果n和num是相等的话,那么就说明每个门都进入了,所以就返回True
                时间复杂度:  O(n+m)
                空间复杂度:  O(n)
'''
def trueCanVisitAllRooms(rooms):
    def dfs(x:int):
        vis.add(x)
        nonlocal num
        num += 1
        for it in rooms[x]:
            if it not in vis:
                dfs(it)
    n = len(rooms)
    num = 0
    vis = set()
    dfs(0)    
    return num == n

'''
    广度优先: 获取一个下标对应的集合就进行处理.
              每进入一个门的话,就会获取出一个值,也就是num ++ , 如果最后 num 加完后的值是与其最初长度相等的话,那么就说明是一样的. 
'''
def breadthCanVisitAllRooms(rooms):
    n = len(rooms)
    num = 0
    vis = {0}
    que = collections.deque([0])
    while que:
        x = que.popleft()
        num += 1
        for it in rooms[x]:
            if it not in vis:
                vis.add(it)
                que.append(it)
    return num == n


if __name__ == "__main__":
    keys = [[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]]
    print(trueCanVisitAllRooms(keys))