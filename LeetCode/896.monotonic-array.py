#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:    
    def isMonotonic(self, nums: [int]) -> bool:
        l = len(nums)
        nums = nums[::-1] if nums[0] > nums[l-1] else nums
        for i in range(l-1):
            if (nums[i] > nums[i + 1]):
                return False
        return True
# @lc code=end
# class Solution:   # 1 = usul
#     def isMonotonic(self, nums: [int]) -> bool:
        #al = []
        # for i in range(len(nums) - 1):
        #     al.append(True if (nums[i] <= nums[i + 1] ) else False)
        #     al.append(True if (nums[i] >= nums[i + 1]) else False)
        # return True if all(al[::2]) or all(al[1::2]) else False

# import numpy as np
# class Solution:    # 2 - usul
#     def isMonotonic(self, nums: [int]) -> bool:
#         nums = nums[::-1] if nums[0] > nums[len(nums)-1] else nums
#         return np.all(np.diff(nums) >= 0)

# class Solution:   #  3 - usul
#     def isMonotonic(self, nums: [int]) -> bool:
#         return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))

m = Solution()
print(m.isMonotonic([6,5,4,4,5]))