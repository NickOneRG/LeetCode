#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (41.45%)
# Likes:    15739
# Dislikes: 4191
# Total Accepted:    2.7M
# Total Submissions: 6.4M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# 
# Example 1:
# 
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, s): 
        w = min(s, key = len)
        res =""
        for i, h in enumerate(w):
            if all(map(lambda si: si[i] == h, s)):
                res += h
            else:
                break
        


        

        return res
              
# @lc code=end



        

