from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        memo = []

        for i in range(1,n+1):
            stack.append("Push")
            memo.append(i)
            if i not in target:
                stack.append("Pop")
                memo.pop(i)
            if memo == target: return stack
        return stack

# @lc code=end

# m = Solution()
# time = t.hisobla()
# print(m.buildArray([1,2], 4))
# # print(call)  
# print(t.hisobla(time,1))

import math
class Solution:
    # def checkTriplet(self,arr, n):
    #     for i, v in enumerate(arr):
    #         a = v ** 2
    #         for z in range(i+1,n):
    #             b = arr[z] ** 2
    #             for d in range(z+1, n):
    #                 print(a,b,arr[d]**2)
    #                 if a + b == arr[d] ** 2: 
    #                     return "Yes"
    #     return "No"
    
    def checkTriplet(self, arr, n):
        maximum = 0
        
        for i in range(n):
            maximum = max(maximum, arr[i])
    
        hash = [0]*(maximum+1)
    
        for i in range(n):
            hash[arr[i]] += 1

        for i in range(1, maximum+1):
            if (hash[i] == 0):
                continue
            for j in range(1, maximum+1):
                if ((i == j and hash[i] == 1) or hash[j] == 0):
                    continue
    
                val = int(math.sqrt(i * i + j * j))
    
                if ((val * val) != (i * i + j * j)):
                    continue
                
                if (val > maximum):
                    continue
    
                if (hash[val]):
                    return "Yes"
        return "No"
    


m = Solution()
time = t.hisobla()
print(m.checkTriplet([3, 8, 5], 3))
# print(call)  
print(t.hisobla(time,1))