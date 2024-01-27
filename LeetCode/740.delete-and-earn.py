import collections
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        res, one, right = 0, collections.Counter(nums), 0
        for i in set(one):
            if not one[i-1]: left, right, res = 0, 0, res + right
                
            left, right = right, max(left + one[i]*i, right)

        return (res + right)
    

# @lc code=end

m = Solution()
time = t.hisobla()
print(m.deleteAndEarn([3,1]))
# print(call)
print(t.hisobla(time, 1))


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memo = dict()
        for v in sorted(nums):
            if v not in memo: memo[v] = 0
            memo[v] += v

        one, two = 0, 0
        for n in memo.values(): 
            one, two, = two, max(one + n, two)
            if two - one > 1: two += one

        return two