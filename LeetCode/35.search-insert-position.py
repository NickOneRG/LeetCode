#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            if target > nums[-1]:
                return len(nums)
            for i in nums:
                if i >= target:
                    return nums.index(i)
                      
# @lc code=end

m = Solution()
print(m.searchInsert([1,3,5,6], 7))