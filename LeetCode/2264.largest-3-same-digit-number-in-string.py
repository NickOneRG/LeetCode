from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2264 lang=python3
#
# [2264] Largest 3-Same-Digit Number in String
#

# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        for n in range(9, -1, -1):
            if (n := str(n)*3) in num: return n 
                
        return ""

# @lc code=end

m = Solution()
time = t.hisobla()
print(m.largestGoodInteger("6777133339"))
# print(call)
print(t.hisobla(time, 1))



# class Solution:
#     def largestGoodInteger(self, num: str) -> str:
#         res, check, count = -1, "", 1
        
#         for v in num:
#             if v == check:
#                 count += 1
#                 if count == 3: res = max(res, int(v))
                    
#             else: check, count = v, 1
                
#         return "000"if res == 0 else str(res)*3 if res != -1 else ""

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(len(num) - 2):
            if len(set(i := num[i:i+3])) == 1:
                res = max(res, i)

        return res
