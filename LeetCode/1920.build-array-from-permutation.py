from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[v] for v in nums]
        
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.buildArray([0, 2, 1, 5, 3, 4]))
print(t.hisobla(time, 1))