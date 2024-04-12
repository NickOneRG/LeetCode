from TestTime import TimeSet
from typing import List
from collections import defaultdict
from heapq import heappush, heapreplace
t = TimeSet()
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#

# @lc code=start
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if (l := len(heights)) == 1:
            return 0

        memo = []
        for i in range(l-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if ladders > 0:
                    heappush(memo, diff)
                    ladders -= 1
                elif memo and memo[0] < diff:
                    bricks -= memo[0]
                    heapreplace(memo, diff)
                else:
                    bricks -= diff

                if bricks < 0: return i
                    
# @lc code=end


time = t.hisobla()

m = Solution()
print(m.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2))

print(t.hisobla(time, 1))
