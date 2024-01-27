from collections import Counter
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2125 lang=python3
#
# [2125] Number of Laser Beams in a Bank
#

# @lc code=start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ind = 0
        for val in bank:
            if (val := val.count('1')) != 0:
                bank[ind] = val 
                ind += 1

        return sum(bank[i-1] * bank[i] for i in range(1, ind))


# @lc code=end


m = Solution()
time = t.hisobla()
print(m.numberOfBeams(["000", "111", "000"]))
# print(call)
print(t.hisobla(time, 1))
