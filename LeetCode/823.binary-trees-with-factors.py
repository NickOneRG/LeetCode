#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#

# @lc code=start
class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        
        for i in range(len(arr)):
            dp[arr[i]] = 1
            for z in range(i):
                if arr[i] % arr[z] == 0:
                    factor = arr[i] // arr[z]
                    if factor in dp:
                        dp[arr[i]] = (dp[arr[i]] + dp[arr[z]] * dp[factor]) % MOD
        
        res = 0
        for v in dp.values():
            res = (res + v) % MOD
        
        return res
        
# @lc code=end

