from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2391 lang=python3
#
# [2391] Minimum Amount of Time to Collect Garbage
#

# @lc code=start
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        fib, memo = 3 * sum(travel), [0] * 3

        # for time in travel: fib.append(fib[-1] + time)

        for i in range(len(garbage)-1, -1, -1):
            v = garbage[i]
            if not memo[0] and "M" in v: fib -= travel[i-2]
            if not memo[1] and "P" in v: fib -= travel[i-2]
            if not memo[2] and "G" in v: fib -= travel[i-2]

            if all(memo): break
        # print(fib[memo[0]], fib[memo[1]], fib[memo[2]])
        return len("".join(garbage)) + fib


# class Solution:
#     def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
#         self.cost = 3 * sum(travel)

#         def check(a_type, i):  
#             while i >= 1:
#                 if a_type in garbage[i]: break
#                 self.cost -= travel[i-1]

#                 i -= 1
#             print(travel[i-1])

#         i = len(garbage)-1
#         for a_type in "MPG":
#             check(a_type, i)
        
#         return self.cost + len("".join(garbage))


        

         
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
#         res, time = 0, 0
#         memo = [-1, -1, -1]

#         for index, value in enumerate(garbage):
#             res += len(value)

#             if "M" in value: memo[0] = index - 1
#             if "P" in value: memo[1] = index - 1
#             if "G" in value: memo[2] = index - 1
                
#         for index, value in enumerate(travel):
#             time += value

#             if memo[0] == index: res += time
#             if memo[1] == index: res += time
#             if memo[2] == index: res += time

#         return res


# class Solution:
#     def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
#         self.res, n = 0, len(garbage)
#         check = [False, False, False]

#         def worker(n, t):
#             check[n]  = True
#             self.res += t

#         for i in range(n-1, -1, -1):
#             gar  = garbage[i]
#             time = sum(travel[:i])

#             if not check[0] and "M" in gar: worker(0, time)
#             if not check[1] and "P" in gar: worker(1, time)
#             if not check[2] and "G" in gar: worker(2, time)

#             if all(check): break

        
#         return self.res + len("".join(garbage))
    