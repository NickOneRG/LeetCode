#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        t = ""
        if len(word1) > len(word2):
            for z in range(len(word2)):
                t += word1[z]
                t += word2[z]
            t += word1[len(word2):len(word1)]
        else:
            for z in range(len(word1)):
                t += word1[z]
                t += word2[z]
            t += word2[len(word1):len(word2)]

        return t
# @lc code=end

m = Solution()
w1, w2 = input().split()
print(m.mergeAlternately(w1, w2))
