from TestTime import TimeSet
from typing import List
t = TimeSet()


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        res = 0
        for x in range(1, n + 1):
            res += m >> 1 if x & 1 else (m + 1) >> 1    
                
        return res



m = Solution()
time = t.hisobla()
print(m.flowerGame(1,5))
# print(call)
print(t.hisobla(time, 1))


