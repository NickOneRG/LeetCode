#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        if len(nums) % 2 == 0:
            return -1
        for i in list(nums):
            if nums.count(i) == 1:
                return i
        return -1    
# @lc code=end

m = Solution()
print(m.singleNumber(list(map(int, input().split()))))