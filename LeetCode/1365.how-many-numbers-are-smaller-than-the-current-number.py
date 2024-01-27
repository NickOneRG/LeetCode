from TestTime import TimeSet
from collections import Counter
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        memo = [0] * 501

        for v in nums: memo[v] += 1
            
        for ind, val in enumerate(nums):
            nums[ind] = sum(memo[:val])
        
        return nums
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.smallerNumbersThanCurrent([8,1,2,2,3]))
# print(call)
print(t.hisobla(time, 1))


