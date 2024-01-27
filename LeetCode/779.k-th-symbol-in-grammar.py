from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count('1') % 2
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.kthGrammar(20, 2))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def kthGrammar(self, n: int, k: int) -> int:
#         res = [0]
#         for i in range(1, n+1):
#             memo = []
#             for z in list(res):
#                 if z == 0:
#                     memo += [0,1]
#                 else:
#                     memo += [1,0]
#             res = memo
#         return res[k-1], len(res)