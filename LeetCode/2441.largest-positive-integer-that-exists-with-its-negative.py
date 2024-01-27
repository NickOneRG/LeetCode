from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        while True:
            res = max(nums)
            if res * -1 in nums: return res   
            else:
                nums.remove(res)
                if nums == []: return -1
               
# @lc code=end


m = Solution()

time = t.hisobla()
print(m.findMaxK( [-1,10,6,8,-7,2]))
# print(call)  
print(t.hisobla(time,1))
