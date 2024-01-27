from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1921 lang=python3
#
# [1921] Eliminate Maximum Number of Monsters
#

# @lc code=start
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        memo = sorted([d / s for d, s in zip(dist, speed)])
        res  = 0

        for i in memo:
            if i > res: res += 1
            else:       return res

        return res

# @lc code=end

m = Solution()
time = t.hisobla()
print(m.eliminateMaximum([1, 2], [100000, 3]))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
#         memo, res = dict(), 1
#         for i in range(len(dist)):
#             memo[i] = round(dist[i] / speed[i], 2)


#         while memo:
#             snipe = min(memo, key= memo.get)
#             memo.pop(snipe)
             
#             if (memo[min(memo, key= memo.get)] if memo != {} else 1) <= 1:
#                 break
#             else:
#                 for i in memo.keys():
#                     memo[i] -= 1
#             res += 1

#         return res
    
# import heapq
# 
# 
# class Solution:
#     def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
#         memo = [round(d / s, 2) for d, s in zip(dist, speed)]
#         memo = sorted(memo)

#         res = 0
#         for i in memo:
#             if i > res: res += 1
#             else:       break  

#         return res
    
