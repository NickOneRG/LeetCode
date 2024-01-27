from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size_n = len(nums) / 2
        for i in set(nums):
            if nums.count(i) > size_n:
                return  i
# @lc code=end



time = t.hisobla()

m = Solution()
print(m.majorityElement([2,2,1,1,1,2,2]))

print(t.hisobla(time, 1))