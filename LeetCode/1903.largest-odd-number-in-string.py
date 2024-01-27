from TestTime import TimeSet
from typing import List
t = TimeSet()

# @lc app=leetcode id=1903 lang=python3
#
# [1903] Largest Odd Number in String
#

# @lc code=start
class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        memo = set("13579")
        
        for i in range(len(num)-1, -1, -1):
            if num[i] in memo: return num[:i+1]
                
        return ""
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.largestOddNumber("35427"))
# print(call)
print(t.hisobla(time, 1))

class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        l = len(num)
        for i in range(l):
            for z in range(l, i, -1):
                if int(num[i:z]) % 2 != 0:
                    return num[i:z]
        return ""