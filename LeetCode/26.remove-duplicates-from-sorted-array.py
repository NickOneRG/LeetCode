#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums:[int]) -> int:
        k = 1
        for z in range(1, len(nums)):
            if nums[z] != nums[z - 1]:
                nums[k] = nums[z]
                k += 1
        return k
# @lc code=end
# for z in range(len(nums)):
# self.nums = list(set(nums))
        # k = len(self.nums)
        # return k
        #     if z < k:
        #         nums.repla
        #         # nums.insert(z, li[z])
        #     else:
        #         nums.pop(k)
        #         # nums.insert(z)
        # return k or nums
m = Solution()
print(m.removeDuplicates(list(map(int, input().split()))))