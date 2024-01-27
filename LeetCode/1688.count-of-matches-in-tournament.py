from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1688 lang=python3
#
# [1688] Count of Matches in Tournament
#

# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        return n - 1

        res = 0
        while n != 1:
            if n % 2 == 0:
                res += (n := n // 2)
                
            else:
                res += (n := (n - 1) // 2)
                n += 1

        return res
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.numberOfMatches(14))
# print(call)
print(t.hisobla(time, 1))

# for i in range(2, 201):
#     print(f"{i} == {m.numberOfMatches(i)}")
    
