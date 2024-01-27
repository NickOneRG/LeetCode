from TestTime import TimeSet
t = TimeSet()
#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: [int]) -> [int]:
        size_n = len(nums) / 3
        new_nums = []
        for i in set(nums):
            if nums.count(i) > size_n:
                new_nums.append(i)
        return new_nums

# @lc code=end

time = t.hisobla()

m = Solution()
print(m.majorityElement([1,2]))

print(t.hisobla(time, 1))