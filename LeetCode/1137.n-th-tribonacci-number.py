from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0, 1, 1] + ([0] * n)

        if n < 3: return 1 if n else 0
        else:
            for i in range(3, n+1):
                memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
            
            return memo[n]

  
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.tribonacci(5))

# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def tribonacci(self, n: int) -> int:
#         zero, one, two = 0, 1, 1

#         if n < 3:
#             return 1 if n else 0
#         else:
#             for _ in range(n-2):
#                 zero, one, two = one, two, zero + one + two

#             return two
