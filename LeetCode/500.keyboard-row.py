from TestTime import TimeSet
from typing import List
import logging
t = TimeSet()
#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        
        res  = []
        for word in words:
            let = set(word.lower())
            if let.issubset(row1) or let.issubset(row2) or let.issubset(row3):
                res.append(word)
        return res
        

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.findWords(["Hello","Alaska","Dad","Peace"]))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:
#         res = []
#         first, second, third = "qwertyuiop", "asdfghjkl", "zxcvbnm"

#         def finder(word: str, keys):
#             for l in word:
#                 if l.lower() not in keys:
#                     return False
#             return True

#         for word in words:
#             if word[0].lower() in first:
#                 if finder(word, first):
#                     res.append(word)

#             elif word[0].lower() in second:
#                 if finder(word, second):
#                     res.append(word)

#             elif word[0].lower() in third:
#                 if finder(word, third):
#                     res.append(word)
#         return res
# 
# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:
#         res  = []
#         rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        
#         for word in words:
#             if any(set(word.lower()) <= row for row in rows):
#                 res.append(word)

#         return res
# 
# 
# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:
#         rows = [{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
#                 {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
#                 {'z', 'x', 'c', 'v', 'b', 'n', 'm'}]
        
#         res  = []
#         for word in words:
#             if any(set(word.lower()).issubset(row) for row in rows):
#                 res.append(word)
#         return res