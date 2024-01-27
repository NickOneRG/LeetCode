from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        try:
            return [0, nums.index(target - nums[0], 1)]
        except:
            res = self.twoSum(nums[1:], target)
            if res is not None:  
                return [i+1 for i in res]
# @lc code=end
        


if __name__ == "__main__":
    m = Solution()
    time = t.hisobla()
    print(m.twoSum([3, 2, 4], 6))
    # print(call)  
    print(t.hisobla(time,1))
    
# class Solution:
#     def twoSum(self, nums, target):        
        
#         for z in list(nums):
#             n = nums.copy()
#             n.remove(z)
#             for i in list(n):
#                 d = z + i
#                 if d == target:
#                     p = nums.index(z)
#                     o = (n.index(i)+1)
#                     return [p,o]  
# 
# class Solution:
    # def twoSum(self, nums, target):        
    #     for i in nums:
    #         res = target - i
    #         if res in nums: return[nums.index(i), nums.index(res)]
    # 

# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             res = target - nums[i]
#             if res in nums[i+1:]: 
#                 return [i, nums.index(res, i+1)]
                