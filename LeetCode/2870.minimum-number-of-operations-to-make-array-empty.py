from collections import Counter
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2870 lang=python3
#
# [2870] Minimum Number of Operations to Make Array Empty
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res, nums = 0, Counter(nums).values()
        
        for val in nums:
            if val == 1: return -1
            res += val // 3 + (val % 3 != 0)

        return res

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]))
# print(call)
print(t.hisobla(time, 1))

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        counter = Counter(nums)

        for _, val in counter.items():
            if val < 2: return -1
            if   val % 3 == 0: res += val // 3
            elif val % 2 == 0: res += val // 2

        return res