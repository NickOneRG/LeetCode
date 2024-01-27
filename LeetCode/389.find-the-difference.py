#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
      
        return list((Counter(t)-Counter(s)).elements())[0]
    
# @lc code=end

m = Solution()
print(m.findTheDifference("ae", "aea"))