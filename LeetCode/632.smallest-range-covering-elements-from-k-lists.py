from typing import List
from collections import defaultdict
#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        memo_d = defaultdict(list)
        for ind, val in enumerate(nums):
            for v in val:
                memo_d[v].append(ind)
        

        keys = sorted(memo_d.keys())
        pointer, n = 0, len(nums)
        
        memo = defaultdict(int)
        left, right = -1, float('Inf')
        have = 0

        for ind in range(len(keys)):
            for x in memo_d[keys[ind]]:
                memo[x] += 1
                if memo[x] == 1:
                    have += 1
                    
            while have == n:
                curr = keys[ind] - keys[pointer]
                if right - left > curr:
                    right = keys[ind]
                    left = keys[pointer]

                for x in memo_d[keys[pointer]]:
                    memo[x] -= 1
                    if memo[x] == 0:
                        have -= 1
                pointer += 1

        return [left, right]
    

# @lc code=end


m = Solution()
print(m.smallestRange([[4, 10,15,24,26],[0,9,12,20],[5,18,22,30]]))