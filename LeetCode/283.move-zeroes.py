#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = nums.count(0)
        nums[:] = [num for num in nums if num != 0]
        nums += [0] * count_zero


# @lc code=end
# class Solution:  # 1st urinish
#     def moveZeroes(self, nums: [int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(nums.count(0)):
#             s = nums.index(0)
#             nums.pop(s)
#             nums.extend([0])
#         # print(nums)
m = Solution()
m.moveZeroes([0,1,0,3,12])