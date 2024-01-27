from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.removeElement([0,1,2,2,3,0,4,2], 2))
# print(call)  
print(t.hisobla(time,1))
