from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        memo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        half_l = len(s) // 2

        return sum(l in memo for l in s[:half_l]) == sum(r in memo for r in s[half_l:])
                

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.halvesAreAlike("book"))
# print(call)
print(t.hisobla(time, 1))