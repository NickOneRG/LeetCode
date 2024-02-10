from TestTime import TimeSet
from typing import List
from collections import defaultdict
import math
t = TimeSet()
#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        res = []
        for i in range((l := len(nums))):
            if nums[i] not in res:
                for j in range(l):

                    if nums[j] not in res and nums[i] != nums[j]:
                        if nums[j] % nums[i] == 0 or nums[i] % nums[j] == 0:
                            res += [nums[i], nums[j]]
                            break
                        
        return res
    

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = defaultdict(set)
        memo[-1]
        
        for i in nums:
            memo[i] = max((memo[j] for j in memo if i % j == 0), key = len) | {i}

        return list(max(memo.values(), key = len))

        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.largestDivisibleSubset([1, 2, 4, 8]))
# print(call)
print(t.hisobla(time, 1))