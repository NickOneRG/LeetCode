from TestTime import TimeSet
from typing import List
from collections import defaultdict
t = TimeSet()
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ev = set()
        tr = set()

        for ever, trus in trust:
            ev.add(ever)
            tr.add(trus)

        res = list(tr - ev)
        
        return res[0] if res else -1
    

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n -1: return -1
            
        ev, tr = [0] * (n+1), [0] * (n+1)
        
        for i, j in trust:
            tr[i] += 1
            ev[j] += 1

        for i in range(1, n+1):
            if ev[i] == n-1 and tr[i] == 0:
                return i
            
        return -1
# @lc code=end


time = t.hisobla()

m = Solution()
print(m.findJudge(3, [[1, 3], [2, 3], [3, 1]]))

print(t.hisobla(time, 1))
