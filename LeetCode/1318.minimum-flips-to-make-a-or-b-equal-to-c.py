#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#

# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        li = []
        lo = [a,b]
        for i in list(lo):
            for z in range(i + 1):
                li.append(bin(z).count("1"))
            return li
# @lc code=end

