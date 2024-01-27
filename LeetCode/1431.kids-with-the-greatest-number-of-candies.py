from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], exCandies: int) -> List[bool]:
        kid = max(candies)

        for i in range(len(candies)):
            candies[i] = True if candies[i] + exCandies >= kid else False

        return candies
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.kidsWithCandies([2,3,5,1,3], 3))
# print(call)
print(t.hisobla(time, 1))