from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        zero, count, res = 0, 0, 0

        for s in range(len(nums)):
            target = nums[s]
            count += target

            while target * (s - zero + 1) - count > k:
                count -= nums[zero]
                zero  += 1

            res = max(res, s - zero + 1)  

        return res

# @lc code=end

m = Solution()
time = t.hisobla()
print(m.maxFrequency([9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966], 3056))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         res, count = 1, 0
        
#         s = nums.pop(0)
#         while nums:
#             zero = nums.pop(0)
#             count += (zero - s) * res
#             s = zero

#             if k >= count:
#                 res += 1
#             else: break

#         return res
    
