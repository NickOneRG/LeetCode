#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        li = []
        lo = []
        for z in range(len(s)):
            if s[z].lower() in "aeiou":
                li.append(z)
            lo.append(s[z])
        lu = li[::-1]
        for i in range(len(li)):
            lo[li[i]] = s[lu[i]]

        d = ''.join(lo)
        return d
# @lc code=end

m = Solution()
print(m.reverseVowels(input()))