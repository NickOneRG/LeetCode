from TestTime import TimeSet
from typing import List
t = TimeSet()


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        die = minutesToTest//minutesToDie

        if die == 1:
            res = buckets - 2
        else:
            for i in range(die):
                


        return res
    


m = Solution()
time = t.hisobla()
print(m.poorPigs(9,15,15))
# print(call)  
print(t.hisobla(time,1))
