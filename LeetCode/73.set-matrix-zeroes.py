from TestTime import TimeSet
from typing import List
t = TimeSet()

# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = [], []
        for ind, val in enumerate(matrix):
            if val.count(0) != 0: row.append(ind)
        
        for ind, val in enumerate(zip(*matrix)):
            if val.count(0) != 0: col.append(ind)

        for i in range(len(matrix)):
            if i in row: 
                matrix[i] = [0] * len(matrix[i])
            else:
                for j in col:
                    matrix[i][j] = 0

        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
# print(call)
print(t.hisobla(time, 1))
