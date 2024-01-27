from collections import Counter
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]:

                    mat[i][j] = min(mat[i-1][j], mat[i][j-1]) + 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if cell := mat[i][j]:

                    mat[i][j] = min(cell, mat[i][j] + 1, mat[i][j] + 1)
        return mat


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # Initialize distances with infinities except for 0s
        distances = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distances[i][j] = 0

        # First pass: update distances from top and left edges
        for i in range(m):
            for j in range(n):
                if i > 0:
                    distances[i][j] = min(distances[i][j], distances[i - 1][j] + 1)
                if j > 0:
                    distances[i][j] = min(distances[i][j], distances[i][j - 1] + 1)

        # Second pass: update distances from bottom and right edges
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    distances[i][j] = min(distances[i][j], distances[i + 1][j] + 1)
                if j < n - 1:
                    distances[i][j] = min(distances[i][j], distances[i][j + 1] + 1)

        return distances

    
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]))
# print(call)
print(t.hisobla(time, 1))


