from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = ([False] * (lengs := len(s))) + [True]

        for i in range(lengs - 1, -1, -1):
            for w in wordDict:
                if (i + (len_w := len(w))) <= lengs and s[i: i + len_w] == w:
                    dp[i] = dp[i + len_w]
                if dp[i]: break

        return dp[0]
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.wordBreak("leetcode", ["leet", "code"]))
print(t.hisobla(time, 1))

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * (l := len(s))
        s = ' ' + s
        wordDict = set(wordDict)
        max_word_len = len(max(wordDict, key=len))

        for i in range(1, l+1):
            for j in range(i-1, max(i-max_word_len-1, -1), -1):
                if dp[j] and s[j+1:i+1] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]
    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * (lengs := len(s))

        for i in range(lengs):
            for j in range(i, lengs):

                if s[i:j+1] in wordDict:
                    dp[j+1] = dp[i] or dp[j+1]

        return dp[-1]