from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2651 lang=python3
#
# [2651] Calculate Delayed Arrival Time
#

# @lc code=start
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        # res = arrivalTime + delayedTime
        # return res if res < 24 else res - 24
        return (arrivalTime + delayedTime) % 24
    
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.findDelayedArrivalTime(13,15))
# print(call)  
print(t.hisobla(time,1))

