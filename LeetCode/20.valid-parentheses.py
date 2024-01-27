#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.19%)
# Likes:    21923
# Dislikes: 1452
# Total Accepted:    3.7M
# Total Submissions: 9.3M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s) :
        par = dict(('()', '[]', '{}'))
        chek = []
        for z in s:
            if z in '([{':
                chek.append(z)
            elif len(chek) == 0 or z != par[chek.pop()]:
                return False
        
        return len(chek) == 0
# @lc code=end
        # dic = {'(': ')', '[': ']', '{':'}'}
        # j, b = 0, 0
        # for z in range(0,len(s), 2):
        #     b = s[z+1]
        #     if dic[s[z]] == b:
        #         j = j + 2
        # return True if len(s) == j else False
        
    
m = Solution()
print(m.isValid(input()))