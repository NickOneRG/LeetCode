from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1269 lang=python3
#
# [1269] Number of Ways to Stay in the Same Place After Some Steps
#

# @lc code=start
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        max_l = min(steps//2 + 1, arrLen)
        dp =[1] + [0]*max_l
        for _ in range(steps):
            prev=0
            for i in range(max_l):
                dp[i], prev =(prev + dp[i] + dp[i + 1]), dp[i]
        return dp[0] % (10**9+7) 


# @lc code=end

rav = []
m = Solution()
for i in range(1001):
    time = t.hisobla()
    print(m.numWays(12, 8))
    # print(call)  
    print(t.hisobla(time,1))
    rav.append(t.rav())
print(f"{sum(rav)/1000:.2f}")


# class Solution:
#     def numWays(self, steps: int, arrLen: int) -> int:
#         mod = (10**9) + 7
#         n = min(arrLen, steps // 2 + 1)
        
#         dp = [0] * n
#         dp[0] = 1

#         while steps > 0:
#             newDp = [0] * n
            
#             for i in range(n):
#                 newDp[i] = dp[i]
                
#                 if i - 1 >= 0: newDp[i] += dp[i - 1]  
                
#                 if i + 1 < n: newDp[i] += dp[i + 1]
                
#                 newDp[i] %= mod
#             dp = newDp
#             steps -= 1

#         return dp[0]
    

# # class Solution:
# #     def numWays(self, steps: int, arrLen: int) -> int:
# #         max_position = min(steps // 2 + 1, arrLen)
# #         cur_ways = [0] * (max_position + 2)
# #         next_ways = [0] * (max_position + 2)
# #         cur_ways[1] = 1
# #         mod = 10 ** 9 + 7

# #         while steps > 0:
# #             for pos in range(1, max_position + 1):
# #                 next_ways[pos] = ((cur_ways[pos] + cur_ways[pos - 1] + cur_ways[pos + 1]) % mod)

# #             cur_ways, next_ways = next_ways, cur_ways
# #             steps -= 1

# #         return cur_ways[1] 