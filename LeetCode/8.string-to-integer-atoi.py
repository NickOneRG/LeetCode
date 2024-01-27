from TestTime import TimeSet
from typing import List
t = TimeSet()

# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int: 
        if not (s := s.lstrip()): return 0

        num = ''
        for val in s[1:] if s[0] in "-+" else s:
            if val.isdigit(): num += val
            else: break

        return max(min(int(s[0]+num if s[0] in "-+" else num), 2**31-1), -2**31)
    

class Solution:
    def myAtoi(self, s: str) -> int:
        if not (s := s.lstrip()) or not s.isdigit(): return 0
            
        num = ''
        for val in s[1:] if s[0] in "-+" else s:
            if val.isdigit(): num += val
            else: break

        return max(min(int(s[0]+num if s[0] in "-+" else num), 2**31-1), -2**31)



# @lc code=end
    

m = Solution()
time = t.hisobla()
print(m.myAtoi("   -42"))
# print(call)
print(t.hisobla(time, 1))

print(True if "" else False)


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        else:
            sign = 1
        res = 0
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        res *= sign
        if res < -2**31:
            return -2**31
        elif res > 2**31 - 1:
            return 2**31 - 1
        else:
            return res
