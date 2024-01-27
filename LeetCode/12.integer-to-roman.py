from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        memo = {
            0: {1: "C", 2:"CC", 3: "CCC", 4:"CD", 5:"D", 6:"DC", 7:"DCC", 8:"DCCC", 9:"CM"},
            1: {1: "X", 2:"XX", 3: "XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX", 8:"LXXX", 9:"XC"},
            2: {1: "I", 2:"II", 3: "III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX"}
            }
        
        res += "M"*(num // 1000)
        for i, v in enumerate([(num % 1000)// 100,(num % 100)// 10,(num % 10)]):
            res += memo.get(i).get(v, "")
       
        return res  
    
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.intToRoman(1994))
# print(call)  
print(t.hisobla(time,1))
# m = Solution()
# res = [False] * 4000
# for i in range(4000):
#     res[i] = m.intToRoman(i)
# time = t.hisobla()
# for i in range(4000):
#     if res[i] != m.intToRoman(i):
#         print("Error!")
# print(call) 
# print(res) 
# print(t.hisobla(time,1))

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         memo = {
#                 1000 : 'M' , 900  : 'CM', 500  : 'D' , 400  : 'CD', 100  : 'C' ,
#                 90   : 'XC', 50   : 'L' , 40   : 'XL', 10   : 'X' , 9    : 'IX',
#                 5    : 'V' , 4    : 'IV', 1    : 'I'   
#             }
        
#         res = ""
#         while num > 0:
#             for i in memo.keys():
#                 if num >= i: break  
#             num -= i
#             res += memo.get(i)
# #         return res
# 
# 
# 
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         res = ""
#         res += "M" * (num // 1000)

#         hundreds = (num % 1000) // 100
#         match hundreds:
#             case 9:
#                 res += "CM"
#             case 4:
#                 res += "CD"
#             case 5:
#                 res += "D"
#             case 6:
#                 res += "DC"
#             case 7:
#                 res += "DCC"
#             case 8:
#                 res += "DCCC"
#             case _:
#                 res += "C" * hundreds

#         tens = (num % 100) // 10
#         match tens:
#             case 9:
#                 res += "XC"
#             case 4:
#                 res += "XL"
#             case 5:
#                 res += "L"
#             case 6:
#                 res += "LX"
#             case 7:
#                 res += "LXX"
#             case 8:
#                 res += "LXXX"
#             case _:
#                 res += "X" * tens

#         ones = (num % 10)
#         match ones:
#             case 9:
#                 res += "IX"
#             case 4:
#                 res += "IV"
#             case 5:
#                 res += "V"
#             case 6:
#                 res += "VI"
#             case 7:
#                 res += "VII"
#             case 8:
#                 res += "VIII"
#             case _:
#                 res += "I" * ones

#         return res  