#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd_length = math.gcd(len(str1), len(str2))
        return str1[:gcd_length]

            
# @lc code=end
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
        
#         lo = list(dict.fromkeys(str1).keys())
#         lu = list(dict.fromkeys(str2).keys())
#         return "".join(lo) if lo == lu else ""

# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if len(str1) < len(str2):
#             str1, str2 = str2, str1  
#         elif str1 + str2 != str2 + str1:
#             return ""  
#         while str2:
#             str1, str2 = str2, str1.replace(str2, "")
#         return str1

m = Solution()
print(m.gcdOfStrings( "ABC","ABCBAD"))