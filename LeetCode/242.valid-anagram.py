from collections import Counter
from TestTime import TimeSet
from typing import List
t = TimeSet()

# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.isAnagram("aaca", "acac"))
# print(call)
print(t.hisobla(time, 1))

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i in t: t = t.replace(i, " ", 1)
            else: return False

        return True if len(s) == len(t) else False