from TestTime import TimeSet
from typing import List
t = TimeSet()

# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
#
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        memo, res = dict(), []
        for i in arr:
            b = str(bin(i))[2:].count('1')
            if b not in memo.keys(): memo[b] = []
            memo[b].append(i)

        for z in sorted(memo.keys()): res += sorted(memo[z])  
        return res
# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x: (bin(x).count('1'), x))


# @lc code=end

m = Solution()
time = t.hisobla()
print(m.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))
# print(call)  
print(t.hisobla(time,1))
# from itertools import combinations
# class Solution:
#     def sumXOR (self, arr, n) : 
#         #Complete the function
#         return sum([i[0]^i[1] for i in combinations(arr,2)])
#         res = 0
#         for i in range(len(arr)):
#             for z in range(i, len(arr)):
#                 s = arr[i] ^ arr[z]
#                 res += s
#         return res

# m = Solution()
# time = t.hisobla()
# print(m.sumXOR([5, 9, 7, 6],1))
# # print(call)  
# print(t.hisobla(time,1))