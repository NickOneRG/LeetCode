from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1413 lang=python3
#
# [1413] Minimum Value to Get Positive Step by Step Sum
#

# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(0, -min(list(sum(nums[:i]) for i in range(1,len(nums)+1)))) + 1
# @lc code=end


m = Solution()

time = t.hisobla()
print(m.minStartValue([1,-2,-3]))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def minStartValue(self, nums: List[int]) -> int:
#         sana = 0
#         while True:
#             sana += 1
#             sana_copy, holat = sana, True
#             for i in nums:
#                 sana_copy = sana_copy + i
#                 if sana_copy < 1:
#                     holat = False
#             if sana_copy >= 1 and holat == True: return sana