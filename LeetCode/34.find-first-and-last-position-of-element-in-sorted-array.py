from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [nums.index(target), len(nums) - 1 - nums[::-1].index(target)] if target in nums else [-1, -1]
       
# @lc code=end

nums = [5,7,7,8,8,10]
target = 8
m = Solution()

time = t.hisobla()

print(m.searchRange(nums, target))

print(t.hisobla(time, 1))


# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         first, last = -1, -1
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 if first == -1:
#                     first = i
#                 last = i
#         return [first, last]