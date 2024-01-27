#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
class Solution:
    def longestStrChain(self, words: [str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i+1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())
  
# @lc code=end

m = Solution()
print(m.longestStrChain(["a","b","ba","bca","bda","bdca","xbc","pcxbcf","xb","cxbc","pcxbc", "exrcfygvbjkj;oiuytc"]))