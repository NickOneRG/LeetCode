from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1887 lang=python3
#
# [1887] Reduction Operations to Make the Array Elements Equal
#

# @lc code=start
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res, prev = 0, nums[0]

        for i, v in enumerate(nums):
            if v < prev:
                res += i
                prev = v
                
        return res

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.reductionOperations([5]))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def reductionOperations(self, nums: List[int]) -> int:
#         def pop_set(p):
#             s = set_n.pop(p)
#             c = max(set_n) if set_n else s
            
#             return [s, c]
        
#         res = 0
#         l = len(nums)
#         set_n = list(set(nums))
#         check = pop_set(set_n.index(max(nums)))

#         while l != sum(nums):
#             m = max(nums)
#             if set_n == []: return res
#             if m == check[1]:
#                 check = pop_set(set_n.index(m))
#             else:
#                 nums[nums.index(m)] = check[1]
#                 res += 1
#         return res