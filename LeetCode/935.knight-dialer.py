from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#

# @lc code=start
class Solution:
    def knightDialer(self, n: int) -> int:
        arr = [1] * 10
        MOD = 10**9 + 7

        for _ in range(n-1):
            arr = [
                (arr[4]+arr[6]) % MOD,
                (arr[6]+arr[8]) % MOD,
                (arr[7]+arr[9]) % MOD,
                (arr[4]+arr[8]) % MOD,
                (arr[3]+arr[9]+arr[0]) % MOD,
                0,
                (arr[1]+arr[7]+arr[0]) % MOD,
                (arr[2]+arr[6]) % MOD,
                (arr[1]+arr[3]) % MOD,
                (arr[2]+arr[4]) % MOD
            ]
            
        return sum(arr) % MOD

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.knightDialer(5000))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def knightDialer(self, n: int) -> int:
#         MOD = 10**9 + 7
#         moves = [
#             [4, 6],
#             [6, 8],
#             [7, 9],
#             [4, 8],
#             [0, 3, 9],
#             [],
#             [0, 1, 7],
#             [2, 6],
#             [1, 3],
#             [2, 4]
#         ]

#         dp = [1] * 10
#         for _ in range(n - 1):
#             dp_new = [0] * 10
#             for digit in range(10):
#                 for move in moves[digit]:
#                     dp_new[move] = (dp_new[move] + dp[digit]) % MOD
#             dp = dp_new

#         return sum(dp) % MOD