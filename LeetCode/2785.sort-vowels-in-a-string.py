from collections import Counter
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2785 lang=python3
#
# [2785] Sort Vowels in a String
#

# @lc code=start
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = sorted([c for c in s if c in "aAeEiIoOuU"])
        return ''.join([vowels.pop(0) if c in "aAeEiIoOuU" else c for c in s])


# @lc code=end

m = Solution()
time = t.hisobla()
print(m.sortVowels("lEetcOde"))
# print(call)  
print(t.hisobla(time,1))

# class Solution:   
#     def sortVowels(self, s: str) -> str:
#         res = list(s)
#         vowels = [125] * len(s)

#         for i, v in enumerate(s):
#             if v in "aAeEoOiIuU" :
#                 vowels[i] = (ord(v))
#         vowels.sort(reverse=True)

#         for i, v in enumerate(s):
#             if v in "aAeEoOiIuU" :
#                 res[i] = chr(vowels.pop())

#         return "".join(res)

    

# class Solution:
#     def sortVowels(self, s: str) -> str:
#         vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
#         count_char = Counter(s)
#         s_vowels = []
#         for char in count_char.keys():
#             if char in vowels:
#                 s_vowels.append(char)
#                 s = s.replace(char, '_')
#         s_vowels.sort()

#         for char in s_vowels:
#             s = s.replace('_', char, count_char[char])
#         return s