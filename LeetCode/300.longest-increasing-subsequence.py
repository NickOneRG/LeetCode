from collections import Counter
from bisect import bisect_left
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        memo, l = [nums[0]], 1

        for num in nums[1:]:
            if num > memo[-1]:
                memo.append(num)
                l += 1

            else: memo[bisect_left(memo, num)] = num  
                
        return l             


# @lc code=end


m = Solution()
time = t.hisobla()
print(m.lengthOfLIS([10,9,2,5,3,7,101,18]))
# print(call)
print(t.hisobla(time, 1))


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = []
        for num in nums:

            if (index := bisect_left(memo, num)) == len(memo):
                memo.append(num)
            else:
                memo[index] = num  
                
        return len(memo) 