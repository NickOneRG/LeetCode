import itertools
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#

# @lc code=start
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        for i in range(2**n):
            i = format(i, '0' + str(n) + 'b')
            if i not in nums:
                return i


# @lc code=end


m = Solution()
time = t.hisobla()
print(m.findDifferentBinaryString(["00000"]))
# print(call)  
print(t.hisobla(time,1))



# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         n = len(nums)
#         nums = set(nums)
#         for i in range(int('1'+'0'*(n-1), 2), int('1'*n, 2)+1):
#             if bin(i)[2:] not in nums:
#                 return bin(i)[2:]
#         return '0'*n
    

# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         num_set = set(nums)
#         n = len(nums[0])

#         for i in range(2**n):
#             bin_str = format(i, '0' + str(n) + 'b')
#             if bin_str not in num_set:
#                 return bin_str
# 
# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         for i in itertools.product('01', repeat=len(nums)):
#             i = ''.join(i)
#             if i not in nums:
#                 return i