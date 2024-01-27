from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1685 lang=python3
#
# [1685] Sum of Absolute Differences in a Sorted Array
#

# @lc code=start
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n, diff = len(nums), sum(nums)

        for i, v in enumerate(nums):
            nums[i] = (2 * i - n) * v + diff
            diff   -= 2 * v

        return nums

    
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.getSumAbsoluteDifferences([1,4,6,8,10]))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
#         res = nums.copy()
#         for i, v in enumerate(nums):
#             summ = 0
#             for j in nums: summ += abs(v - j)
                
#             res[i] = summ
#         print(sum(nums))
#         return res
    
# class Solution:
#     def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         res = [0] * n

#         l_sum, r_sum = 0, sum(nums)

#         for i in range(n):
#             res[i] = i * nums[i] - l_sum + r_sum - (n - i) * nums[i]
#             l_sum += nums[i]
#             r_sum -= nums[i]

#         return res
    
