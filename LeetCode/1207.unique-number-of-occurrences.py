from collections import Counter
from TestTime import TimeSet
from typing import List
t = TimeSet()

# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        return len(set(count := Counter(arr).values())) == len(count)
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
# print(call)
print(t.hisobla(time, 1))
