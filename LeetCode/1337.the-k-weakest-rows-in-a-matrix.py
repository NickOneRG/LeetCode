
#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: [[int]], k: int) -> [int]:
        li = [(sum(row), i) for i, row in enumerate(mat)]
        li.sort()
        return [(li[z][1]) for z in range(k)]
# @lc code=end

m = Solution()
s = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
print(m.kWeakestRows(s,3))