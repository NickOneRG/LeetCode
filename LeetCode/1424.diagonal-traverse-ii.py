from collections import defaultdict
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1424 lang=python3
#
# [1424] Diagonal Traverse II
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        memo, res = [], []
        
        for i, v in enumerate(nums):
            for z, val in enumerate(v):
                
                if len(memo) <= i + z: memo.append([])
                memo[i + z].append(val)
                
        for i in memo: res += reversed(i)
            
        return res
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7],
      [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
       
#         res = []
#         l = len(nums)
#         inside_l = len(max(nums, key=len))
            
#         for i in range(l):
#             for z in range(i+1):
#                 try:
#                     res.append(nums[i - z][z])
#                 except: pass

#         nums.reverse()
#         s = []
#         for i in range(l-1):
#             for z in range(i+1):
#                 try:
#                     s.append(nums[i-z][::-1][z])
#                 except: pass
#         res += reversed(s)
    
#         return res   