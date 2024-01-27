from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        memo = 0
        for ind, val in enumerate(nums):
            nums[ind] = (memo := memo + val)

        return nums        

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.runningSum([1, 2, 3, 4]))
# print(call)
print(t.hisobla(time, 1))


