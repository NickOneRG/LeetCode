#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> [[int]]:
        lu = []
        for i in range(1, numRows+1):        
            a = 1
            li = []
            for z in range(1, i+1):
                li.append(a)
                a = a * (i - z) // z
            lu.append(li)
        return lu
# @lc code=end

m = Solution()
print(m.generate(5))