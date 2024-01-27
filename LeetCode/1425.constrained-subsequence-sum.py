from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1425 lang=python3
#
# [1425] Constrained Subsequence Sum
#

# @lc code=start
# import heapq
# class Solution:
#     def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
#         heap = [(-nums[0], 0)]
#         res = nums[0]
        
#         for i in range(1, len(nums)):
#             while i - heap[0][1] > k:
#                 heapq.heappop(heap)

#             curr = max(0, -heap[0][0]) + nums[i]
#             res = max(res, curr)
#             heapq.heappush(heap, (-curr, i))

#         return res
    
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        memo, dp = [], [0] * len(nums)
        res = float('-inf')

        for i in range(len(nums)):
            while memo and i - memo[0][1] > k:
                memo.pop(0)

            dp[i] = nums[i]
            if memo: dp[i] = max(dp[i], memo[0][0] + nums[i])
                
            while memo and dp[i] > memo[-1][0]:
                memo.pop()

            memo.append((dp[i], i))
            res = max(res, dp[i])

        return res



# @lc code=end

m = Solution()
time = t.hisobla()
print(m.constrainedSubsetSum([-5266,4019,7336,-3681,-5767], 2))
# print(call)  
print(t.hisobla(time,1))

# from sortedcontainers import SortedList

# class Solution:
#     def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
#         window = SortedList([0])
#         dp = [0] * len(nums)
        
#         for i in range(len(nums)):
#             dp[i] = nums[i] + window[-1]
#             window.add(dp[i])
#             if i >= k:
#                 window.remove(dp[i - k])
        
#         return max(dp)