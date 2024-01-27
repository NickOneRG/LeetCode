from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = dict()

        for i, n in enumerate(nums):
            if n in memo and abs(i - memo[n]) <= k:
                return True
            else: memo[n] = i
                
        return False


# @lc code=end


m = Solution()
time = t.hisobla()
print(m.containsNearbyDuplicate([1, 2, 3, 1], 3))
print(t.hisobla(time, 1))


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i, v in enumerate(nums):
            memo = nums[i+1:]
            if v in memo:
                if abs(i - (i+1 + memo.index(v))) <= k:
                    return True
        return False