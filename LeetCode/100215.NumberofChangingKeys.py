from collections import Counter
from TestTime import TimeSet
from typing import List
t = TimeSet()

class Solution:
    def countKeyChanges(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            if s[i].lower() != s[i+1].lower(): res += 1
        return res


m = Solution()
time = t.hisobla()
print(m.countKeyChanges("aAbBcC"))
# print(call)
print(t.hisobla(time, 1))
