from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1727 lang=python3
#
# [1727] Largest Submatrix With Rearrangements
#

# @lc code=start
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:

        for j in range(len(matrix[0])):
            for i in range(1, len(matrix)):
                matrix[i][j] += matrix[i-1][j] if matrix[i][j] else 0


        for i, v in enumerate(matrix):
            v.sort(reverse= True)

            for ind, val in enumerate(v):
                v[ind] = (ind +1) * val

            matrix[i] = max(v)

        return max(matrix)
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))
# print(call)  
print(t.hisobla(time,1))

# class Solution: # not working code 
#     def largestSubmatrix(self, matrix: List[List[int]]) -> int:
#         res = [0] * len(matrix[0])
#         row = [0] * len(matrix)
#         for i, v in enumerate(matrix):
#             row[i] += sum(v)
#             for ind, val in enumerate(v):
#                 res[ind] += val
#         res.sort()
#         row.sort()

#         return res, row