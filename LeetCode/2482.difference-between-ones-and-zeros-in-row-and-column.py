from TestTime import TimeSet
from typing import List
t = TimeSet()

# @lc app=leetcode id=2482 lang=python3
#
# [2482] Difference Between Ones and Zeros in Row and Column
#

# @lc code=start
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        column = [sum(col) for col in zip(*grid)]
        
        for ind, row in enumerate(grid):
            zero = m - (row := sum(row))
            
            grid[ind] = [(row + col) - zero - (n - col) for col in column]

        return grid

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
# print(call)
print(t.hisobla(time, 1))


        # for row in grid:
        #     print(row)

        # for col in zip(*grid):
        #     print(col)

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for ind, val in enumerate(words):
            if x in val:
                res.append(ind)
        return res