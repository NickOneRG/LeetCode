#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        i = 0
        for z in nums:
            if i < 2 or z > nums[i-2]:
                nums[i] = z
                i += 1
        return i
# @lc code=end

m = Solution()
print(m.removeDuplicates(list(map(int, input().split()))))