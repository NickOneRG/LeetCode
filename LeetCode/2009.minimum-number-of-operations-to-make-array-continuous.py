from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2009 lang=python3
#
# [2009] Minimum Number of Operations to Make Array Continuous
#

# @lc code=start
import bisect
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        len_nums = len(nums)
        nums = sorted(set(nums))
        res = 10**9

        for i in range(len(nums)):
            res = min(res, len_nums - (bisect.bisect_right(nums, (nums[i] + len_nums - 1)) - i))
            
        return res

 
# @lc code=end

m = Solution()

time = t.hisobla()
print(m.minOperations([41,33,29,33,35,26,47,24,18,28]))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         nums = sorted(set(nums))
#         left, res = 0, 0
#         for right in range(len(nums)):
#             while nums[right] - nums[left] >= len(nums):
#                 left += 1
#             res = max(res, right - left + 1)
#         return len(nums) - res
    
# from collections import Counter
# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         nums.sort()
#         counter = Counter(nums)
#         left, max_l = 0, 0
#         len_n = len(nums)

#         for right in range(len_n):
#             while nums[right] - nums[left] >= len_n:
#                 counter[nums[left]] -= 1
#                 if counter[nums[left]] == 0:
#                     del counter[nums[left]]
#                 left += 1
#             max_l = max(max_l, right - left + 1)

#         return len_n - max_l
# 
# from collections import Counter
# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         len_true = len(nums)-1
#         max_num = max(nums)
#         min_num = min(nums)
#         counter = Counter(nums)
#         res = 0
#         step = 0
#         sum_val = sum(counter.values())

#         if max_num - min_num  == len_true and sum_val == len_true:
#             return 0
#         else:
#             con_nums = list(counter.keys())
#             max_num = len_true + min_num
#             len_con_nums = len(con_nums)

#             for i in range(len_con_nums):
#                 if con_nums[step] > max_num:
#                     res += 1
#                     con_nums.remove(con_nums[step])
#                 else:
#                     step += 1
#                 pass
#             return max_num, res + (sum_val - len_con_nums)