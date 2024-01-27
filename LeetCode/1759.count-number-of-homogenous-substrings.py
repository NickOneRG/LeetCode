from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1759 lang=python3
#
# [1759] Count Number of Homogenous Substrings
#
from itertools import groupby
# @lc code=start
class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        modul = 10 ** 9 + 7
        for k, g in groupby(s):
            n = len(list(g))
            res += ((n * (n + 1)) // 2) % modul

        return res

    
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.countHomogenous("abbcccaa"))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def countHomogenous(self, s: str) -> int:
#         res     = 0
#         same_or = check = ""
#         for i in s:
#             if i != check:
#                 same_or = ""
#             same_or += i
            
#             res += len(same_or)
#             check = i
        
#         modul = 10 ** 9 + 7
#         return res % modul

# class Solution:
#     def countHomogenous(self, s: str) -> int:
#         modul = 10 ** 9 + 7
#         check = ""
#         res,count = 0, 0

#         for i in s:
#             if i == check: count += 1   
#             else:          count = 1
                
#             res   = (res + count) % modul
#             check = i

#         return res
