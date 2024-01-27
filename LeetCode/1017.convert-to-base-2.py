#
# @lc app=leetcode id=1017 lang=python3
#
# [1017] Convert to Base -2
#

# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        res = ""
        while n:
            res += str(n & 1)
            n = -(n >> 1)
        return res[::-1] if len(res) != 0 else "0"

# @lc code=end
        if n == 0:
            return '0'
        res = ""
        while n != 0:
            n, m = divmod(n, -2)
            if m < 0:
                n, m = n + 1, m + 2
            res += str(m)
        return res[::-1]
m = Solution()
print(m.baseNeg2(int(input())))