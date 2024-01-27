from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1561 lang=python3
#
# [1561] Maximum Number of Coins You Can Get
#

# @lc code=start
class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        res, l = 0, len(piles)
        counter = l-1

        piles.sort()
        for _ in range(l//3):
            counter -= 1
            res += piles[counter] 
            counter -= 1
        
        return res

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.maxCoins([2, 4, 1, 2, 7, 8]))
# print(call)  
print(t.hisobla(time,1))
