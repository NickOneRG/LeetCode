from TestTime import TimeSet
from itertools import pairwise
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1637 lang=python3
#
# [1637] Widest Vertical Area Between Two Points Containing No Points
#

# @lc code=start
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        for ind, val in enumerate(points):
            points[ind] = val[0]
        points.sort(reverse=True)

        for i in range(1, len(points)):
            points[i-1] = points[i-1] - points[i]
        
        return max(points[:-1])


# class Solution:
#     def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
#         return max(b-a for (a, _), (b, _) in pairwise(sorted(points)))

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
# print(call)
print(t.hisobla(time, 1))

print(int('+15'))