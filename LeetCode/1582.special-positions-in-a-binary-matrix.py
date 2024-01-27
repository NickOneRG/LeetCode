from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0

        for row in mat:
            if sum(row) == 1:
                ind = row.index(1)
                if sum(row[ind] for row in mat) == 1:
                    res += 1

        return res
            

# @lc code=end

m = Solution()
time = t.hisobla()
print(m.numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
# print(call)
print(t.hisobla(time, 1))


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        memo = [0] * len(mat[0])

        for ind, row in enumerate(mat):
            for ind, val in enumerate(row):
                if val:
                    memo[ind] += 1
                    if memo[ind] == 1: res += 1
            if sum(row) < 1: res -= sum(row)
        return res
    


