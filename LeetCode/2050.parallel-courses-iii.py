from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2050 lang=python3
#
# [2050] Parallel Courses III
#

# @lc code=start
from collections import defaultdict
from graphlib import TopologicalSorter
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = defaultdict(set)
        for prv,nxt in relations:
            g[prv].add(nxt)
        
        for i in TopologicalSorter(g).static_order():
            time[i-1] += max((time[j-1] for j in g[i]),default=0)
        return max(time)
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.minimumTime(5,[[1,5],[2,5],[3,5],[3,4],[4,5]], [1,2,3,4,5]))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
#         max_ = max(relations, key = lambda x: x[1])
#         res = []
#         rel = max_[1]
#         for i in relations[::-1]:
#             if i[1] == max_[1]: res.append(sum(i))
#             elif i[1] == max_[0]: res.append(sum(i+max_))
#         return res

# from collections import defaultdict, deque
# class Solution:
#     def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
#         memo, memo_D = defaultdict(list), [0] * n
#         dqua, res = deque([]), [0] * n
         
#         for p, nx in relations:
#             p, nx = p - 1, nx - 1  
#             memo[p].append(nx)
#             memo_D[nx] += 1

#         for i in range(n):
#             if memo_D[i] == 0:
#                 dqua.append(i)
#                 res[i] = time[i]
        
#         while dqua:
#             i = dqua.popleft()
#             for v in memo[i]:
#                 res[v], memo_D[v] = max(res[i] + time[v], res[v]), memo_D[v] - 1
#                 if memo_D[v] == 0: dqua.append(v)
                    

#         return max(res)