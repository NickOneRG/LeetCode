from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1793 lang=python3
#
# [1793] Maximum Score of a Good Subarray
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = right =  k
        res  = min_v =  nums[k]
        len_n = len(nums)
        
        while left > 0 or right < len_n - 1:
            if left == 0 or (right < len_n - 1 and nums[right + 1] > nums[left - 1]): right += 1
            else: left -= 1
                
            min_v = min(min_v, nums[left], nums[right])
            res   = max(res, min_v * (right - left + 1))
        
        return res
        
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.maximumScore([1,4,3,7,4,5], 3))
# print(call)  
print(t.hisobla(time,1))