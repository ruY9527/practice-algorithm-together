'''
    拥有最多糖果的孩子
    https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/
'''

'''
    该题目就是先获取出最大的数值. 
    然后对集合的数据进行迭代,每次迭代的值和extraCandies相加,如果相加后都值大于等于 最大数值,那么就是True
'''
def kidsWithCandies(candies,extraCandies):
    record_data = max(candies)
    bolList = []
    for i in range(0,len(candies)):
        if candies[i] + extraCandies >= record_data:
            bolList.append(True)
        else:
            bolList.append(False)    
    return bolList
    #pass

if __name__ == "__main__":
    #candies = [2,3,5,1,3]
    #extraCandies = 3   
    candies = [12,1,12]
    extraCandies = 10
    blList = kidsWithCandies(candies,extraCandies) 
    print(blList)