from collections import Counter
from TestTime import TimeSet
from typing import List
t = TimeSet()
# 
# @lc app=leetcode id=1347 lang=python3
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#

# @lc code=start
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        
        for  v in set(s):
            num_t = t.count(v)
            num_s = s.count(v)
            
            if num_t < num_s: res += (num_s - num_t)

        return res
        
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.minSteps("leetcode", "practice"))
# print(call)
print(t.hisobla(time, 1))


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s, count_t = Counter(s), Counter(t)
        res = 0
        
        for  k, v in count_s.items():
            num = count_t.get(k)
            if num == None: res += v
            elif num < v:   res += (v - num)

        return res