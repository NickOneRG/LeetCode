from TestTime import TimeSet
from typing import List
t = TimeSet()
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        common = set(text1) & set(text2)

        if len(common) == 0: return 0

        text1 = [c for c in text1 if c in common]
        text2 = [c for c in text2 if c in common]

        if len(text1) > len(text2): text1, text2 = text2, text1
            
        dp = [0 for _ in text1]

        for text in text2:
            count = 0
            for i in range(len(text1)):
                if count < dp[i]: count = dp[i]
                    
                elif text == text1[i]:
                    dp[i] = count + 1

        return max(dp)
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.longestCommonSubsequence("ezupkr", "ubmrapg"))
# print(call)
print(t.hisobla(time, 1))

# print(len(str(999**999)))

print(len(bin(999**999)[2:])//8)
