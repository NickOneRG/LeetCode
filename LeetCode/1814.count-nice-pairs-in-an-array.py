from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1814 lang=python3
#
# [1814] Count Nice Pairs in an Array
#

# @lc code=start
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev_f(val):
            rev = 0
            while val > 0:
                rev = rev * 10 + val % 10
                val //= 10
            return rev
        
        res, count, MOD = 0, {}, 10**9 + 7

        for n in nums:
            rev  = rev_f(n)
            cur  = count.get(n - rev, 0)
            res += cur % MOD
            count[n - rev] = 1 + cur

        return res % MOD
    
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.countNicePairs([13, 10, 35, 24, 76]))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def countNicePairs(self, nums: List[int]) -> int:
#         def count( val):
#             rev = 0
#             while val > 0:
#                 rev = rev * 10 + val % 10
#                 val //= 10
#             return rev
        
#         rev_nums = [count(val) for val in nums]

#         MOD = 10**9 + 7
#         res = 0

#         for i in range(len(nums)-1):
#             check = True
#             for num, rev in zip(nums[i:], rev_nums[i:]):
#                 if check:
#                     gen, rev_g, check = num, rev, False
                
#                 else:
#                     if gen + rev == num + rev_g:
#                         res += 1

#         return res % MOD