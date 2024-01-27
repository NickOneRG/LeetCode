from TestTime import TimeSet
from typing import List
t = TimeSet()

#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack, cur, op = [], 0, '+'

        for c in s + '+':
            if c.isdigit(): cur = (cur * 10) + int(c)
            elif  c in "+-*/":
                match op:
                    case "-": stack.append(-cur)
                    case "+": stack.append(cur)
                    case "*": stack.append(stack.pop() * cur)
                    case "/": stack.append(int(stack.pop() / cur)) 
                cur, op = 0, c  
        return sum(stack)
    

# @lc code=end

m = Solution()
time = t.hisobla()
print(m.calculate("14-3/2"))
# print(call)  
print(t.hisobla(time,1))


# diferens = 0   
#             for i in range(len(res)):
#                 i = i - diferens
#                 if res[i] in "/*":
#                     if res[i] == "*":
#                         jav = int(res[i-1]) * int(res[i+1])
#                     else:
#                         jav = int(res[i-1]) // int(res[i+1])

#                     res.pop(i-1)
#                     res.pop(i-1)
#                     res.pop(i-1)
#                     res.insert(i-1, str(jav))
#                     diferens += 2

                # if "*" not in res and "/" not in res: break
                # 
# class Solution:
#     def calculate(self, s: str) -> int:
#         res = []
#         b = ""
#         for i in s:
#             if i not in "+-*/":
#                 b += i
#             else:
#                 res.append(b)
#                 res.append(i)
#                 b = ""
#         res.append(b)


#         while "*" in res or "/" in res:
#             if "*" in res: mul = res.index("*") 
#             else:          mul = 3 * (10**5)
#             if "/" in res: div = res.index("/")
#             else:          div = 3 * (10**5)
                
#             if mul < div: 
#                 operator = mul
#                 jav = int(res[mul -1]) * int(res[mul +1])
#             else: 
#                 operator = div
#                 jav = int(res[div -1]) // int(res[div +1]) 

#             res.pop(operator-1)
#             res.pop(operator-1)
#             res.pop(operator-1)
#             res.insert(operator-1, str(jav))
        
#         while len(res) != 1:
#             if res[1] in "+-":
#                 if  res[1] == "-": jav = int(res[0]) - int(res[2])
#                 else:              jav = int(res[0]) + int(res[2])
                    
#                 res.pop(0)
#                 res.pop(0)
#                 res.pop(0)
#                 res.insert(0, str(jav))
                

#         return int(res[0])
    
