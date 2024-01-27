from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = nums + [0]

        for i in range(len(nums)-3, -1, -1):
            nums[i] = max(nums[i] + nums[i+2], nums[i+1])

        return nums[0]


# @lc code=end


m = Solution()
time = t.hisobla()
print(m.rob([2, 7, 9, 3, 1]))
# print(call)  
print(t.hisobla(time,1))

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
            
        one, two = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            two, one = max(two, one + nums[i]), two

        return two