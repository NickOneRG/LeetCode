from typing import List
#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)

        return nums[2] if len(nums) > 2 else max(nums)
        
# @lc code=end

m = Solution()
print(m.thirdMax([2,1]))

t = 26
relay =  None
if t < 27:
    relay = True

elif t > 29:
    relay = False

print(relay)