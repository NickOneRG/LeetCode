#
# @lc app=leetcode id=2696 lang=python3
#
# [2696] Minimum String Length After Removing Substrings
#

# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for i in s:
            if stack and stack[-1] + i in ["AB", "CD"]:
                stack.pop()
            else:
                stack.append(i)

            
        return len(stack)

# @lc code=end

m = Solution()
print(m.minLength("ABFCACDB"))
