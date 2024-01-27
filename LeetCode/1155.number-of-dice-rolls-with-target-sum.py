from TestTime import TimeSet
from collections import defaultdict
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#

# @lc code=start
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        if target <  n or n*k  < target : return 0
        if target == n or n*k == target : return 1

        MOD, memo, start = 10**9+7, [1] + [0] * target,  max(target - k, 0)
        
        for _ in range(n):  
            memo[target] = (mem := sum(memo[i] for i in range(start, target)) % MOD)
            
            for tar in range(target-1, -1, -1):
                if tar - k >= 0: mem += memo[tar-k]
                    
                mem -= memo[tar]
                memo[tar] = mem

        return memo[target] % MOD


# @lc code=end


m = Solution()
time = t.hisobla()
print(m.numRollsToTarget(30, 30, 500))
# print(call)
print(t.hisobla(time, 1))


    
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def engine(dp: list, n: int, k: int, target: int) -> int:
            mod = 10 ** 9 + 7
            if target == 0 and n == 0: return 1
            if n == 0 or target <= 0 : return 0
                
            if dp[n][target] != -1: return dp[n][target] % mod
                
            ways = 0
            for i in range(1, k + 1):
                ways = (ways + engine(dp, n - 1, k, target - i)) % mod
    
            dp[n][target] = ways % mod
            return dp[n][target]
        
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        return engine(dp, n, k, target)
    
    
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = defaultdict(int)
        dp[0] = 1

        for _ in range(n):
            memo = defaultdict(int)
            for i in range(target+1):
                memo[i] = memo[i-1] + dp[i]
            for i in range(target+1):
                dp[i] = (memo[i-1] - memo[i-k-1]) % MOD
            

        return dp[target]
    
# class Solution:
#     def numRollsToTarget(self, n: int, k: int, target: int) -> int:

#         if target <  n or n * k  < target: return 0
#         if target == n or n * k == target: return 1

#         MOD = 10**9 + 7
#         dp = [[0] * (target + 1) for _ in range(n + 1)]

#         dp[0][0] = 1  

#         for i in range(1, n + 1):
#             for j in range(target + 1):
#                 for roll in range(1, k + 1):
#                     if j >= roll:
#                         dp[i][j] = (dp[i][j] + dp[i - 1][j - roll]) % MOD

#         return dp[n][target]