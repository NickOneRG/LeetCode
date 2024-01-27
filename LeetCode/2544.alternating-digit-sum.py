from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2544 lang=python3
#
# [2544] Alternating Digit Sum
#

# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res, sign = 0, 1
        for value in str(n):
            res, sign = res + sign * int(value), -sign
        return res
        
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.alternateDigitSum(5215165156))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def alternateDigitSum(self, n: int) -> int:
#         res = 0
#         for index, value in enumerate(str(n)):
#             value = int(value)
#             res += value if index % 2 == 0 else -value 
#         return res
