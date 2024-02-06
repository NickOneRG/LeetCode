from TestTime import TimeSet
from typing import List
from collections import Counter, defaultdict
t = TimeSet()
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (l := len(s)) < (count := len(t)): return ""
            
        start = 0
        res   = (0, float('inf'))
        memo  = defaultdict(int)

        for char in t: memo[char] += 1

        for ind, val in enumerate(s):
            if memo[val] > 0: count -= 1
                
            memo[val] -= 1
            if not count:
                while memo[s[start]]:
                    
                    memo[s[start]] += 1
                    start += 1

                if ind - start < res[1] - res[0]:
                    res = (start, ind)

                memo[s[start]] += 1
                count += 1
                start += 1

        return "" if res[1] > l else s[res[0] : res[1] + 1]
    


# @lc code=end


m = Solution()
time = t.hisobla()
print(m.minWindow("ADOBECODEBANC", "ABC"))
# print(call)
print(t.hisobla(time, 1))


# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if (l := len(s)) < len(t): return ""

#         def f(ch = 0):

#             check = 0
#             left, right = 0, l
#             while True:
#                 for i in t:
#                     if i not in s: break

#                 else:
#                     if check: left += 1
#                     else: right -= 1

#                     s = s[left: right]
#                     continue 

#                 if check: break
#                 check = 1
            
        
#         res = [f(), f()]  

#         return res[0] if len(res[0] < len(res[1])) else res[0]


