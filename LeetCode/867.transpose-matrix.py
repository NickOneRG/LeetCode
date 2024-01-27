from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        return list(list(val[i] for val in matrix) for i in range(len(matrix[0])))
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.transpose([[1, 2, 3], [4, 5, 6]]))
# print(call)
print(t.hisobla(time, 1))


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []

        for i in range(len(matrix[0])):
            l = []
            for val in matrix:
                l.append(val[i])
            res.append(l)

        return res



