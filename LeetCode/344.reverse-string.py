#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s:[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        x = s[::-1]

        for z in range(len(s)):
            s[z] = x[z]


# @lc code=end
        return s

m = Solution()
print(m.reverseString(list(input().split())))
