from TestTime import TimeSet
from typing import List
from collections import defaultdict
t = TimeSet()

# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:  # First Approaches  ==> too slow O(n^2)
    def firstUniqChar(self, s: str) -> int:
        
        for ind, val in enumerate(s):
            if s.count(val) == 1: return ind

        return -1
    

class Solution:  # Second Approaches  ==> optimized
    def firstUniqChar(self, s: str) -> int:

        res = {1: -1}
        memo = ""

        for i in s[::-1]:
            if i not in memo:
                res[s.count(i)] = s.find(i)
                memo += i

        return res[1]


class Solution:  # Third Approaches  ==> another way to solve a problem
    def firstUniqChar(self, s: str) -> int:

        memo = ""

        for ind, val in enumerate(s):
            if val not in memo:
                if s.count(val) == 1: 
                    return ind
                memo += val

        return -1
    

class Solution:  # Fourth Approaches  ==> without using the count
    def firstUniqChar(self, s: str) -> int:
        memo = {}

        for i, char in enumerate(s):
            memo[char] = -1 if char in memo else i

        for i in memo.values():
            if i != -1: return i

        return -1

        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.firstUniqChar("leetcode"))
# print(call)
print(t.hisobla(time, 1))
