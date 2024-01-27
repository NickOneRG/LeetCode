#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> [int]:
        li = []
        for z in range(n + 1):
            li.append(bin(z).count("1"))
        return li

# @lc code=end

m = Solution()
print(m.countBits(int(input())))
