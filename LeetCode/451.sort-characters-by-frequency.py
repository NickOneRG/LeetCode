from TestTime import TimeSet
from typing import List
from collections import defaultdict, Counter
t = TimeSet()
#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        group = dict()

        for key, val in Counter(s).items():
            if val not in group:
                group[val] = [key]
            else:
                group[val].append(key)

        res = ""
        for key in sorted(group.keys(), reverse=True):
            for val in sorted(group[key]):
                res += val * key

        return res

        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.frequencySort("treeAabb"))
# print(call)
print(t.hisobla(time, 1))