from typing import List
from heapq import heappush, heappop
#
# @lc app=leetcode id=1942 lang=python3
#
# [1942] The Number of the Smallest Unoccupied Chair
#

# @lc code=start
class Pair:
    def __init__(self, end_time, idx):
        self.end = end_time
        self.idx = idx

    def __lt__(self, x):
        return self.end < x.end


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [(x, i) for i, x in enumerate(times)]
        times.sort(key=lambda x: x[0][0])
        pointer = 0
        chairs, memo = [], []
        
        for (come, go), idx in times:
            
            while memo and come >= memo[0].end:
                pair = heappop(memo)
                heappush(chairs, pair.idx)
            if not chairs:
                chair = pointer
                pointer += 1
            else:
                chair = heappop(chairs)
            heappush(memo, Pair(go, chair))
            if idx == targetFriend:
                return chair
# @lc code=end



m = Solution()
print(m.smallestChair([[3, 10],[1,5],[2,6]], 0))



