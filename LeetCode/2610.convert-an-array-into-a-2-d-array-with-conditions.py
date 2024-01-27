from collections import Counter
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2610 lang=python3
#
# [2610] Convert an Array Into a 2D Array With Conditions
#

# @lc code=start
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res = [[] for _ in range(max(counter.values()))]

        for num, count in counter.items():
            for i in range(count):
                res[i].append(num)

        return res



# @lc code=end


m = Solution()
time = t.hisobla()
print(m.findMatrix([1,3,4,1,2,3,1]))
# print(call)
print(t.hisobla(time, 1))


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        
        return [[j for j in counter.keys() if counter[j] >= i] for i in range(1, max(counter.values())+1)]
    




class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []

        for num in nums:
            found = True
            for group in res:
                print(group)
                if num in group:
                    continue
                else:
                    found = False
                    group.add(num)
                    break

            if found:
                res.append(set([num]))

        return res
    