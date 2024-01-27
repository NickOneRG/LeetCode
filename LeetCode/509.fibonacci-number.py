from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        pre, nex = 0, 1
        for _ in range(n):
            pre, nex = nex, pre + nex
        return pre
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.fib(99))
# print(call)  
print(t.hisobla(time,1))
