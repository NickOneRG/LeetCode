from collections import defaultdict
from TestTime import TimeSet
from typing import List
t = TimeSet()

#
# @lc app=leetcode id=1743 lang=python3
#
# [1743] Restore the Array From Adjacent Pairs
#

# @lc code=start
class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        res = []

        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                res = [node, neighbors[0]]
                break

        while len(res)   < len(pairs) + 1:
            last, prev   = res[-1], res[-2]
            candidates   = graph[last]
            next_element = candidates[0] if candidates[0] != prev else candidates[1]

            res.append(next_element)

        return res
    

# @lc code=end

m = Solution()
time = t.hisobla()
print(m.restoreArray([[4, -2], [1, 4], [-3, 1]]))
# print(call)  
print(t.hisobla(time,1))

