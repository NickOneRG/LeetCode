from collections import defaultdict
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1074 lang=python3
#
# [1074] Number of Submatrices That Sum to Target
#

# @lc code=start
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        res, len_m = 0, len(matrix[0])

        for row in matrix:
            for col in range(1, len_m):
                row[col] += row[col-1]

        for col in range(len_m):
            for k in range(col, len_m):
                cur_sum, memo = 0, defaultdict(int)
                memo[0] = 1

                for row in matrix:
                    cur_sum += row[k] - (row[col-1] if col >= 1 else 0)

                    if cur_sum-target in memo:
                        res += memo[cur_sum-target]
                    if cur_sum in memo:
                        memo[cur_sum] += 1
                    else:
                        memo[cur_sum] = 1

        return res
    
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))
# print(call)
print(t.hisobla(time, 1))