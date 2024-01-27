from TestTime import TimeSet
from typing import List
t = TimeSet()

# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        zero, one, total1 = 0, 0, s.count('1')

        res = 0
        for c in s:
            if c == '1': one += 1
            else: zero += 1

            if res < (val := zero + total1-one): res = val   

        return res
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.maxScore("1111"))
# print(call)
print(t.hisobla(time, 1))


class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            if (val := s[:i].count('0') + s[i:].count('1')) > res:
                res = val

        return res
