#
# @lc app=leetcode id=2525 lang=python3
#
# [2525] Categorize Box According to Criteria
#

# @lc code=start
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        categ = "Neither"
        volume = 1
        for cat in [length, width, height]:
            if cat >= 100_000:
                categ = "Bulky"
                break
            volume *= cat
            
        if volume >= 10**9:
            categ = "Bulky"
        
        if mass >= 100:
            categ = "Both" if categ == "Bulky" else "Heavy"
        
        return categ
            
# @lc code=end

m = Solution()
print(m.categorizeBox(length=1000, width=35, height=700, mass=300))
