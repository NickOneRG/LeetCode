from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1630 lang=python3
#
# [1630] Arithmetic Subarrays
#

# @lc code=start
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        memo_che = []

        # for quer_l, quer_r in zip(l, r):
        #     memo  = sorted(nums[quer_l: quer_r+1])
        #     check = True
        
        for i in range(len(nums)-1):
            if (nums[i+1] - nums[i] != nums[1] - nums[0]):
                memo_che.append(False)
                
            else: memo_che.append(True)

        return memo_che

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.checkArithmeticSubarrays([4,6,5,9,3,7], [0,0,2], [2,3,5]))
# print(call)  
print(t.hisobla(time,1))
# class Solution:
#     def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
#         res, memo = [], []
#         prev = nums[0]
#         next = nums[1]
#         check = False

#         for quer_l, quer_r in zip(l, r):
#             memo = sorted(nums[quer_l: quer_r], reverse= True)
#             prev, next = memo[-1], 0
#             check = True
#             for i in memo:
#                 dif = prev - i
#                 if dif != 0 or next != dif: break

#                 prev, next = i, dif

#             else: check = False 
#             res.append(check)
#         return res
# 
# 
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(nums):
            nums.sort()
            return all(nums[i+1] - nums[i] == nums[1] - nums[0] for i in range(len(nums)-1))

        return [check(nums[i:j+1]) for i, j in zip(l, r)]

