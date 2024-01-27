from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2251 lang=python3
#
# [2251] Number of Flowers in Full Bloom
#

# @lc code=start
import bisect
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start, end = [], []
        for fl_start, fl_end in flowers:
            start.append(fl_start)
            end.append(fl_end)
        start = sorted(start)
        end = sorted(end)

        return [bisect.bisect_right(start, i) - bisect.bisect_left(end, i) for i in people]

# @lc code=end


m = Solution()

time = t.hisobla()
print(m.fullBloomFlowers([[19,37],[19,38],[19,35]], [6,7,21,1,13,37,5,37,46,43]))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
#         s = 0
#         res = []
#         res_dic = dict()
#         for i in flowers:
#             if i[1] > s:
#                 s = i[1]
#         for z in range(1,s+1):   
#             res_dic[z] = 0
#         for i in flowers:
#             for z in range(i[0], i[1]+1):
#                 res_dic[z] += 1 
#         for i in people:
#             try:
#                 res.append(res_dic[i])
#             except :
#                 res.append(0)
                
#         return res
# 
# class Solution:
#     def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
#         res_dic = dict()
#         for i in flowers:
#             for z in range(i[0], i[1]+1):
#                 res_dic[z] = res_dic.get(z, 0) + 1
#         return [res_dic.get(i, 0) for i in people]