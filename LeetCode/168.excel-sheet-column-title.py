#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
from functools import lru_cache
class Solution:
    @lru_cache
    def convertToTitle(self, columnNumber: int) -> str:
        return '' if columnNumber == 0 else self.convertToTitle((columnNumber-1) // 26) + chr(((columnNumber-1) % 26) + ord('A'))
        
    

# @lc code=end

# class Solution:   # 1 - usul but not working after about 18100
#     def convertToTitle(self, columnNumber: int) -> str:
#         s = columnNumber // 26
#         if columnNumber + 64 <= ord("Z"):
#             return chr(columnNumber + 64)
#         elif columnNumber <= 702:
#             c = columnNumber % 26
#             return chr(s+64) + chr(c+64) if c != 0 else chr(s+63) + chr(c+90) 
#         else:
#             c = columnNumber % 26
#             a = s // 26
#             b = s % 26
#             return (chr(a+64) + chr(b+90) + chr(c+64) if  c != 0 else chr(a+63) + chr(b+90) + chr(c+90)) if c == 0 or b == 0  else  chr(a+64) + chr(b+64) + chr(c+64)#, a,b,c

# res = ""   #2 - usul !!! Not Finished !!!
#         ch = []
#         while columnNumber > 0:
#             b = columnNumber%26
#             columnNumber = columnNumber // 26
#             ch.append([columnNumber,b])
#             b += 90 if b == 0 else 64
#             if columnNumber != 1:
#                 res += chr(b)
#             # ch.append([b, chr(b)])
#         print(ch)
#         return res[::-1]
m = Solution()
print(m.convertToTitle(int(input())))

# while True: