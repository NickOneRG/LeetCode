from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checker(start,end):
            while(start>=0 and end<len(s) and s[start]==s[end]):
                start -= 1
                end   += 1
            return(s[start +1 : end])
        
        res = ""
        for i in range(len(s)):
            len_res = len(res)

            check = checker(i,i)
            if len_res < len(check): res = check
                
            check = checker(i,i+1)
            if len_res < len(check): res = check
                
        return res
            
        
        
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.longestPalindrome("babaddtattarrattatddetartrateedredividerb"))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 1: return s
#         res, len_s = "", len(s)
#         for i in range(len_s):
#             for z in range(len_s+1, i, -1):
#                 pal = s[i:z] 
#                 check = (pal == pal[::-1])

#                 if check and len(pal) > len(res):   res  = pal
#                 elif check and len(pal) < len(res): return res
        
#         return res

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if s == s[::-1]: return s
            
#         left  = self.longestPalindrome(s[1:])
#         right = self.longestPalindrome(s[:-1])

#         return left if len(left) > len(right) else right