from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        memo = [[], []]

        for ind, val in enumerate([s,t]):
            for i in val:
                if i != '#':    memo[ind].append(i)   
                elif memo[ind]: memo[ind].pop()  

        return memo[0] == memo[1]
        

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.backspaceCompare("ab#c", "ad#c"))
# print(call)  
print(t.hisobla(time,1))