from typing import List
import heapq
#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg, pos = 0, len(nums)
        heapq.heapify(nums)

        for num in nums:
            if num < 0:
                neg += 1
                pos -= 1
            elif num == 0:
                pos -= 1
            else:
                break

        return max(neg, pos)
                 
    
# @lc code=end

m = Solution()
print(m.maximumCount([-3, -2,-1,0,0,1,2]))




# class Solution: # Not completed yet
#     def maximumCount(self, nums: List[int]) -> int:
#         neg, pos = 0, len(nums)
#         heapq.heapify(nums)
#         check = True

#         for ind, num in enumerate(nums):
#             if num == 0:
#                 if check:
#                     check = False
#                     neg = ind
#                 pos -= 1
        
#         neg = len(nums[:neg])

#         return max(neg, pos-neg)