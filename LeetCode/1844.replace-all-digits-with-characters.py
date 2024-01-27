from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        
        for ind, val in enumerate(s := list(s), -1):
            if val.isdigit():
                s[ind+1] = chr(ord(s[ind]) + int(val))


        return "".join(s)
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.replaceDigits("a1c1e1"))
# print(call)
print(t.hisobla(time, 1))
