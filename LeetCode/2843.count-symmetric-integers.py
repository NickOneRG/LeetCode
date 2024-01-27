from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2843 lang=python3
#
# [2843]   Count Symmetric Integers
#

# @lc code=start
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for num in range(low, high+1):
            num     = str(num)
            len_sym = len(num)

            if len_sym % 2 == 0:
                half = len_sym // 2

                left_sum  = sum(int(digit) for digit in num[:half])
                right_sum = sum(int(digit) for digit in num[half:])

                if left_sum == right_sum: res += 1

        return res

    
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.countSymmetricIntegers(1200,1230))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def countSymmetricIntegers(self, low: int, high: int) -> int:
#         res = 0
#         for i in range(low, high+1):
#             i = str(i)
#             len_sym = len(i)

#             if len_sym % 2 == 0:
#                 len_sym = len_sym // 2
#                 res_mini = 0

#                 for ind, val in enumerate(i):
#                     val = int(val)

#                     if ind < len_sym: res_mini += val
#                     else:             res_mini -= val

#                 if res_mini == 0:
#                     res += 1
                    
#         return res

