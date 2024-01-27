from TestTime import TimeSet
from typing import List
t = TimeSet()

# @lc app=leetcode id=2706 lang=python3
#
# [2706] Buy Two Chocolates
#

# @lc code=start
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        prices.remove(min_c := min(prices))
        sum_p = money - (min_c + min(prices))

        return sum_p if sum_p > -1 else money
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.buyChoco([3, 2, 3], 3))
# print(call)
print(t.hisobla(time, 1))
