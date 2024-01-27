#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        res = [[0] * k for k in range(1, query_row + 3)]
        res[0][0] = poured
        for i in range(query_row + 1):
            for z in range(i+1):
                q = (res[i][z] - 1.0) / 2.0
                if q > 0:
                    res[i+1][z] += q
                    res[i+1][z+1] += q

        return min(1, res[query_row][query_glass])

# @lc code=end
# class Solution:
#     def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
#         res = [[0] * k for k in range(1, 102)]
#         res[0][0] = poured
#         for i in range(query_row + 1):
#             for z in range(i+1):
#                 q = (res[i][z] - 1.0) / 2.0
#                 if q > 0:
#                     res[i+1][z] += q
#                     res[i+1][z+1] += q

#         return min(1, res[query_row][query_glass])
m = Solution()
print(m.champagneTower(100000009,33,17))