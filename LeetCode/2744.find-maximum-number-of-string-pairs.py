from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2744 lang=python3
#
# [2744] Find Maximum Number of String Pairs
#

# @lc code=start
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        res = 0
        for ind, val in enumerate(words):
            for z in range(ind+1, len(words)):
                if val[::-1] == words[z]:
                    res += 1
                    break

        return res  
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))
# print(call)
print(t.hisobla(time, 1))