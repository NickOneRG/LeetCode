#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mul = 1
        if len(columnTitle)  == 1:
            return (ord(columnTitle)-64)
        else:
            for i in columnTitle:
                mul_copy = mul
                s = (ord(i)-64)
                mul += 26*s
                s += mul_copy
        
        return s
# @lc code=end

m = Solution()

print(m.titleToNumber(input()))