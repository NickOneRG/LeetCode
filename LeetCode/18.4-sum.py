from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
from itertools import permutations
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        li = []
        for i in range(len(nums)-3):
            perms = permutations(nums[i:i+4])
            print(nums[i:i+4])
            def check_sum_greater_than_k(perm):
                print(sum(perm))
                return sum(perm) == target

            # Use filter function
            filtered_perms = list(filter(check_sum_greater_than_k, perms))
            li.extend(filtered_perms)
        


        return set(li)
# @lc code=end



time = t.hisobla()

m = Solution()
print(m.fourSum([1,0,-1,0,-2,2], 0))

print(t.hisobla(time, 1))