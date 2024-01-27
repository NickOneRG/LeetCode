#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res, memo = [0], []
#         counter = 0
#         for i in s:
#             if i in memo:
#                 res.append(counter)
#                 counter = 1
#             else:
#                 counter +=1
#                 memo.append(i)
#         return max(res + [counter])
# @lc code=start    
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        memo, counter, res = {}, 0, 0
        
        for r in range(len(s)):
            char = s[r]
            if char in memo and memo[char] >= counter: counter = memo[char] + 1     
            else: res = max(res, r - counter + 1)
                
            memo[char] = r
        return res
# @lc code=end

m = Solution()
print(m.lengthOfLongestSubstring("dvdf"))