from TestTime import TimeSet
from bisect import bisect_right, bisect_left
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        ind = 0
        for e, s, p in sorted(zip(endTime, startTime, profit)):
            startTime[ind] = s
            endTime[ind]   = e
            profit[ind]    = p
            ind += 1
        
        for i in range(1, len(profit)):

            index = bisect_right(endTime, startTime[i]) - 1
            profit[i] = max(profit[i - 1], (profit[index] if index >= 0 else 0) + profit[i])

        return profit[-1]
    
     # dp = [profit[0]] + ([0] * ((n := )-1))
# @lc code=end

# m = Solution()
# time = t.hisobla()
# print(m.jobScheduling( [1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))
# # print(call)
# print(t.hisobla(time, 1))

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        dp = [[0,0]]
        f = lambda x: dp[bisect_left(dp,[x+1])-1][1]

        for end, start, pro in sorted(zip(endTime,startTime, profit)):  

            dp.append([end, max(f(end),pro+f(start))])

        return dp[-1][1] 
    

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        endTime, startTime, profit = zip(*sorted(zip(endTime, startTime, profit)))
        
        dp = [profit[0]] + ([0] * ((n := len(profit))-1))

        for i in range(1, n):

            index = bisect_right(endTime, startTime[i]) - 1
            dp[i] = max(dp[i - 1], (dp[index] if index >= 0 else 0) + profit[i])

        return dp[-1] 
    

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        res = 0
        
        while x != y:
            if x % 11 == 0: x = x // 11
            
            elif x % 5 == 0: x = x // 5
            
            elif x in [4, 9, 10] and x > y: x += 1
            
            else: x -= 1
                
            
            res += 1
            
        return res
    
m = Solution()
time = t.hisobla()
print(m.minimumOperationsToMakeEqual(54, 2))
# print(call)
print(t.hisobla(time, 1))



