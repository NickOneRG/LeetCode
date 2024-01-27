from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle)-2, -1, -1):
            for col in range(0, len(triangle[row])):

                triangle[row][col] += min(triangle[row+1][col+1], triangle[row+1][col])

        return triangle[0][0]
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         triangle[0] = triangle[0][0]
#         wich = 0

#         for ind in range(1, len(triangle)):

#             if triangle[ind][wich] > triangle[ind][wich+1]:  wich += 1 

#             triangle[ind] = triangle[ind][wich]

#         print(triangle)
#         return sum(triangle)
    
