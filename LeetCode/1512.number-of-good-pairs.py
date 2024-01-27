from typing import List
from TestTime import TimeSet
t = TimeSet()
#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
from itertools import combinations
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_d = dict()
        res = 0
        for i in range(len(nums)):
            if nums[i] not in count_d:
                count_d[nums[i]] = [i]
            else:
                count_d[nums[i]].append(i)
        for z in count_d.keys():
            sana = count_d[z]
            len_sana = len(sana)
            if len_sana == 1:
                pass
            elif len_sana == 2:
                res += 1
            else:
                res += len(list(combinations(sana, 2)))
        return res
# @lc code=end

time = t.hisobla()

m = Solution()
print(m.numIdenticalPairs([1,2,3,1,1,3]))

print(t.hisobla(time, 1))


