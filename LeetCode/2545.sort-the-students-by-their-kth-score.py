from TestTime import TimeSet
from typing import List
t = TimeSet()
#
#
# @lc app=leetcode id=2545 lang=python3
#
# [2545] Sort the Students by Their Kth Score
#

# @lc code=start
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key = lambda x: x[k])
        return score[::-1]
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
#         memo, res = dict(), []
#         for i in score:
#             memo[i[k]] = i
#         for i in sorted(memo)[::-1]:
#             res.append(memo[i])
            
#         return res