from TestTime import TimeSet
from typing import List
from collections import Counter
import math
t = TimeSet()
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        memo = [i**2 for i in range(1, 101) if i**2 < n]

        def check(num: int) -> bool:
            return math.floor(math.sqrt(num)) ** 2 == num

        if check(n): return 1

        nums = set()
        for mem in memo:
            nums.add(n - mem)

        res = 1
        while nums:
            nums_in = set()
            for num in nums:
                if check(num):return res + 1

                for mem in memo:
                    if mem > num: break
                    if mem not in nums_in:
                        nums_in.add(num - mem)

            nums = nums_in
            res += 1

        return res


        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.numSquares(12))
# print(call)
print(t.hisobla(time, 1))
