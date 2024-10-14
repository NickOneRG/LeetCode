from math import floor, ceil
from typing import List
import heapq
#
# @lc app=leetcode id=2530 lang=python3
#
# [2530] Maximal Score After Applying K Operations
#

# @lc code=start
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        nums = [-num for num in nums]
        heapq.heapify(nums)

        score = 0
        for _ in range(k):
            score -= heapq.heappushpop(nums, floor(nums[0]/3))

        return score
    

# @lc code=end

m = Solution()
print(m.maxKelements( [1, 10,3,3,3], 3))




# class Solution:
#     def maxKelements(self, nums: List[int], k: int) -> int:

#         max_heap = [(-num, i) for i, num in enumerate(nums)]
#         heapq.heapify(max_heap)

#         score = 0
#         for _ in range(k):
#             _, i = heapq.heappop(max_heap)
#             score += nums[i]
#             nums[i] = ceil(nums[i] / 3)
#             heapq.heappush(max_heap, (-nums[i], i))

#         return score

