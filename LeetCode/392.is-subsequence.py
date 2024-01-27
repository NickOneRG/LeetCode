#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            if char not in t:
                return False
            t = t[t.index(char) + 1:]
        return True
# @lc code=end

m = Solution()
print(m.isSubsequence("leeeeetcode","yylyyeyeyyeyeyeyytycyoydye"))