from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        res, selector = 0, s[0]
        for i in range(1, len(s)):
            if (i := s[i]) == selector: 
                res += 1 
                selector = 0 if i=='1' else 1
                
            else: selector = i
            
        return res
    

class Solution:
    def minOperations(self, s: str) -> int:
        res, selector = 0, "0"
        
        for char in s:
            if char != selector: res += 1
                
            selector = "1" if selector == "0" else "0" 

        return res
    

class Solution:
    def minOperations(self, s: str) -> int:
        res1, res2 = 0, 0
        selector1, selector2 = "0", "1"

        for char in s:
            if char != selector1: res1 += 1
            if char != selector2: res2 += 1
                
            selector1 = "1" if selector1 == "0" else "0"
            selector2 = "1" if selector2 == "0" else "0"

        return min(res1, res2)
    

class Solution:
    def minOperations(self, s: str) -> int:
        res, sel = 0, True

        for char in s:
            if sel == (char == "0"): res += 1

            sel = not sel

        return min(res, len(s) - res)


# @lc code=end

m = Solution()
time = t.hisobla()
print(m.minOperations("01001"))
# print(call)
print(t.hisobla(time, 1))

