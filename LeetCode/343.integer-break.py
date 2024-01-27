from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n > 5:
            max_d = n-1
            for i in range(2,int(n/2)):
                roun = round(n/i)
                max_d = max(max_d,(roun**(i-1)) * (n-roun*(i-1)))
            return max_d
        if n <= 3:
            return n - 1
        return 4 if n==4 else 6
            
        
# @lc code=end
for z in range(3):
    inp = int(input("Enter = "))
    timefor = t.hisobla()
    m = Solution()
    for i in range(2,inp):
        time = t.hisobla()
        print(m.integerBreak(i),t.hisobla(time, 1))
    print(t.hisobla(timefor, 1))


# class Solution:
#     def integerBreak(self, n: int) -> int:
#         diferens = 0
#         if n > 3:
#             for z in range(n, 0, -1):
#                 floor_d = n // z
#                 modulo = n % z
#                 last_ho = n - z
#                 # print((floor_d * (z - 1)) + (floor_d + modulo))
#                 la = 0
#                 if ((z * floor_d) + floor_d) == n:
#                     la = (z ** floor_d) * floor_d 
#                 res = max(diferens, last_ho * z,la,(floor_d ** (z-1)) * (floor_d + modulo))
#                 diferens = res
#                 # print(res)
#             return res
#         else:
#             return 1 if n == 2 else 2
# 
# class Solution:
    # def integerBreak(self, n: int) -> int:
    #     max_d = [0]*(n+1)
    #     max_d[1] = 1
    #     for i in range(2, n+1):
    #         for z in range(1, i):
    #             max_d[i] = max(max_d[i], max(z*(i-z), z*max_d[i-z]))
    #     return max_d[n]