#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i[::-1] for i in s.split()])
        
# @lc code=end
# new_s = ""
#         for i in s.split():
#             print(i)
#             new_s += i[::-1]
#       
#       # s = s.split() # 2 - usul
        # return "".join(s[i][::-1]+(" " if i != len(s)-1 else "") for i in range(len(s)))
        
#         return new_s
m = Solution()
print(m.reverseWords("hehe hehe hehe hehe"))