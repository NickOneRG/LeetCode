from typing import List
#
# @lc app=leetcode id=2496 lang=python3
#
# [2496] Maximum Value of a String in an Array
#

# @lc code=start
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
    
        for i in strs:
            s = int(i) if i.isdigit() else len(i)
            res = s if s > res else res
            
        return res
     
        
# @lc code=end

m = Solution()
print(m.maximumValue(["alic3", "bob","3","4","00000"]))