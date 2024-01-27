#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x =''.join(filter(str.isalnum, s)).lower()
        return True if x[::-1] == x else False 



# @lc code=end

m = Solution()
print(m.isPalindrome(input()))