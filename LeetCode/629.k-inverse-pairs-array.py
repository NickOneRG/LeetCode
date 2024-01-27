from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=629 lang=python3
#
# [629] K Inverse Pairs Array
#

# @lc code=start
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp, MOD = [1]+[0] * k, 10 ** 9 + 7
        
        for i in range(n):
            memo, count = [], 0
            for j in range(k + 1):
                count += dp[j]
                if j-i >= 1: count -= dp[j-i-1]
                
                memo.append(count % MOD)
                
            dp = memo
           
        return dp[k]
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.kInversePairs(9, 15))
# print(call)
print(t.hisobla(time, 1))


print(int(input()) + int(input()))
