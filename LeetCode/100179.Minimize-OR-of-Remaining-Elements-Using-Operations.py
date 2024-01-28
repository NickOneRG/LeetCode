import heapq
from functools import reduce
from operator import or_
from TestTime import TimeSet
from typing import List
t = TimeSet()


class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        while k > 0 and len(nums) > 1:
            a = -heapq.heappop(nums)
            b = -heapq.heappop(nums)
            k -= 1

            heapq.heappush(nums, -(a & b))

        return -heapq.heappop(nums)


sol = Solution()
print(sol.minOrAfterOperations([3, 5, 3, 2, 7], 2)) 
print(sol.minOrAfterOperations([7, 3, 15, 14, 2, 8], 4)) 
print(sol.minOrAfterOperations([10, 7, 10, 3, 9, 14, 9, 4], 1)) 


class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:

        result = reduce(or_, nums)

        for i in range(31):
            if result & (1 << i) == 0:
                continue  

            pairs = 0
            for num in nums:
                if num & (1 << i):  pairs += 1
                   
            pairs = min(pairs, k)
            result &= ~(1 << i)

            k -= pairs

            if k == 0: break
                
        return result


m = Solution()
time = t.hisobla()
print(m.minOrAfterOperations([10, 7, 10, 3, 9, 14, 9, 4], 1))
# print(call)
print(t.hisobla(time, 1))
sol = Solution()

print(sol.minOrAfterOperations([3, 5, 3, 2, 7], 2))  
print(sol.minOrAfterOperations([7, 3, 15, 14, 2, 8], 4))  
print(sol.minOrAfterOperations([10, 7, 10, 3, 9, 14, 9, 4], 1))  
