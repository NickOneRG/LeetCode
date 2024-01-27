from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res, prev = 0, -1
        for i in timeSeries:
            res += duration - (prev - i + 1) if i <= prev else duration
            prev = i + duration - 1
        return res


# @lc code=end  

m = Solution()

time = t.hisobla()
print(m.findPoisonedDuration([1,2], 2))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
#         if not timeSeries:
#             return 0

#         total = 0
#         end = timeSeries[0] + duration
#         for i in range(1, len(timeSeries)):
#             if timeSeries[i] < end:
#                 total += timeSeries[i] - timeSeries[i-1]
#             else:
#                 total += duration
#             end = timeSeries[i] + duration

#         return total + duration
# 
# 
# class Solution:
#     def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
#         res = set()
#         for i in timeSeries:
#             for z in range(duration):
#                 res.add(i)
#                 i += 1
#         return len(res)