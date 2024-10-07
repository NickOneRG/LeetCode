#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        s = 0
        for char in columnTitle:
            s = s * 26 + ord(char) - 65 +1
        return s
    
# @lc code=end

m = Solution()

for i in ["A", "B", "C", "D", "E", "F", "Z", "AA", "AB", "AZ", "ZY", "FXSHRXW"]:
    print(f"{i}:  {m.titleToNumber(i)}")
