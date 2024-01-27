from TestTime import TimeSet
from typing import List
import math
t = TimeSet()
#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n):
        if n == 0: return False

        while n != 1:
            if n % 4 != 0: return False
            n //= 4

        return True

# @lc code=end

m = Solution()
time = t.hisobla()
print(m.isPowerOfFour(1))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def isPowerOfFour(self, n):
#         for i in range(16):
#             res = 4 ** i
#             if res == n: return True
#             if res >  n: return False
                
#         return False

