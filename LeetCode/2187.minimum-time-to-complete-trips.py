from typing import List
#
# @lc app=leetcode id=2187 lang=python3
#
# [2187] Minimum Time to Complete Trips
#

# @lc code=start
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        res = 0
        trips = 0
        count = 1
        while trips <= totalTrips:
            for i in time:
                if count % i == 0:
                    trips += 1
            count += 1
            res += 1

        return res



class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        a, b = 1, totalTrips * min(time)

        def f(x):
            return sum(x // t for t in time) >= totalTrips
    
        while a < b:
            m = (a + b) // 2
            if not f(m): a = m + 1
            else: b = m
        return a
    
# @lc code=end

m = Solution()
print(m.minimumTime([2], 1))