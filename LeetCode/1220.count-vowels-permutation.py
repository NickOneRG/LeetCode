from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#

# @lc code=start  
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        a = e = i = o = u = 1
        
        for _ in range(1, n):
            a, e, i, o, u = e, (a + i) % mod, (a + e + o + u) % mod, (i + u) % mod, a

        return (a + e + i + o + u) % mod

# @lc code=end

m = Solution()
time = t.hisobla()
print(m.countVowelPermutation(200000))
# print(call)  
print(t.hisobla(time,1))


