#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        d = set()
        for i, z in enumerate(s):
            if z not in d:
                while stack and stack[-1] > z and stack[-1] in s[i:]:
                    d.remove(stack.pop())
                stack.append(z)
                d.add(z)
        return ''.join(stack)


# @lc code=end

# from collections import Counter
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         for z in sorted(set(s)):
#             suf = s[s.index(z):]
#             if set(s) == set(suf):
#                 return z + self.removeDuplicateLetters(suf.replace(z, ''))
#         return ""
# ch = True
#         for z in list(s):
#             if s.count(z) == 1 and ch == True:
#                 ind = s.index(z)
#                 ch = False
#         s = s[ind:len(s)]
#         b = "".join(dict.fromkeys(s).keys())
       
#         return b
m = Solution()
print(m.removeDuplicateLetters("cbacdcbc"))