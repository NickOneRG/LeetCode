from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1420 lang=python3
#
# [1420] Build Array Where You Can Find The Maximum Exactly K Comparisons
#

# @lc code=start
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        dict_ = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
        for j in range(1, m+1):
            dict_[1][j][1] = 1
        for i in range(2, n+1):
            for j in range(1, m+1):
                for z in range(1, min(k, i)+1):
                    dict_[i][j][z] = (dict_[i][j][z] + dict_[i-1][j][z]*j + sum(dict_[i-1][jj][z-1] for jj in range(1, j))) % mod
        return sum(dict_[n][j][k] for j in range(1, m+1)) % mod



# @lc code=end


n = 9
m = 1
k = 1

# Call the function
m = Solution()

time = t.hisobla()

print(m.numOfArrays(n, m, k))

print(t.hisobla(time, 1))



# class Solution:
#     def numOfArrays(self, n: int, m: int, k: int) -> int:

#         MOD = 10**9 + 7
#         dic_ = {}

#         def helper(indx, curr_max, cost):
#             if (indx, curr_max, cost) in dic_:
#                 return dic_[(indx, curr_max, cost)]

#             if indx == 1 and cost == 1:
#                 return 1
#             elif indx == 1 or cost == 0:
#                 return 0

#             nWay = 0
#             for j in range(1, m + 1):
#                 if j <= curr_max:
#                     nWay += helper(indx - 1, curr_max, cost)
#                 else:
#                     nWay += helper(indx - 1, j, cost - 1)
#             dic_[(indx, curr_max, cost)] = nWay % MOD

#             return dic_[(indx, curr_max, cost)]

#         res = 0
#         for j in range(1, m + 1):
#             res = (res + helper(n, j, k)) % MOD

#         return res