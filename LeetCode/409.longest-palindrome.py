#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)
        g = set()
        l = list()
        for z in s:
            g.add(z)
        g = list(g)
        for z in list(g):
            l.append(s.count(z))
        p = 1
        for z in list(l):
            if z == 1:
                l.remove(1)
                if p == 1:
                    l.append(1)
                    p = 0
            elif z % 2 > 0 :
                if p == 1:
                    p = 0
                else:
                    l.append(-1)
        return sum(l)

# @lc code=end

#counter

m = Solution()
print(m.longestPalindrome(input()))