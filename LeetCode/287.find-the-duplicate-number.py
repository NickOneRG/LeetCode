#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
import math

class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        n = len(nums)
        bitset = [0 for _ in range(n)]

        for num in nums:
            if bitset[num] == 1:
                return num
            bitset[num] = 1

        return -1


# @lc code=end
# class Solution:
#     def findDuplicate(self, nums: [int]) -> int:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return num
#             seen.add(num)

m = Solution()
print(m.findDuplicate(list(map(int, input().split()))))