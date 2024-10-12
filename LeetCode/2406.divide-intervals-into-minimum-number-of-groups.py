from typing import List
from heapq import heappush, heappop
#
# @lc app=leetcode id=2406 lang=python3
#
# [2406] Divide Intervals Into Minimum Number of Groups
#

# @lc code=start
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        res = []

        for start, end in sorted(intervals, key=lambda x: x[0]):
            if res and res[0] < start:
                heappop(res)
                
            heappush(res, end)

        return len(res)

        
# @lc code=end


m = Solution()
print(m.minGroups([[5, 10],[6,8],[1,5],[2,3],[1,10]]))