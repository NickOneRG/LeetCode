from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1611 lang=python3
#
# [1611] Minimum One Bit Operations to Make Integers Zero
#

# @lc code=start
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        div = 16

        while div:
            n ^= n >> div
            div //= 2

        return n

# @lc code=end

m = Solution()
time = t.hisobla()
print(m.minimumOneBitOperations(51651516))
print(t.hisobla(time, 1))
    

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        n ^= n >> 16
        n ^= n >> 8
        n ^= n >> 4
        n ^= n >> 2
        n ^= n >> 1
        
        return n
    

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0

        while n:
            res ^= n
            n  >>= 1
        
        return res