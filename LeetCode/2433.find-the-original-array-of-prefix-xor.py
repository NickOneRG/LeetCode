from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2433 lang=python3
#
# [2433] Find The Original Array of Prefix Xor
#

# @lc code=start
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        xor = 0
        for num in pref: 
            res.append(num ^ xor)
            xor = num
        return res


# @lc code=end

m = Solution()
time = t.hisobla()
print(m.findArray([5,2,0,3,1]))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def findArray(self, pref: List[int]) -> List[int]:
#         res = [pref[0]]
#         if len(pref) == 1: return res
        
#         for i in range(1,len(pref)):
#             memo = pref[0]
#             for z in range(1,len(res)):
#                 memo ^= res[z] 
#             memo ^= pref[i]
#             res.append(memo)
# #         return res
# 
# 
# 
# class Solution:
#     def findArray(self, pref: List[int]) -> List[int]:
#         res, xor = [pref[0]], pref[0]
        
#         for i in range(1, len(pref)):
#             res.append(xor ^ pref[i])
#             xor ^= res[i]
            
#         return res