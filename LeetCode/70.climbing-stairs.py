#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
from time import perf_counter

# @lc code=start
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         return int(((1.618033988749895 ** (n + 1) - (-1.618033988749895) ** -(n + 1)) / 2.23606797749979)//1)
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n):
            two, one = one + two, two
        return one    
    
    # from math import sqrt
    # sqrt(5) == 2.23606797749979
    # (1 + sqrt(5)) / 2 == 1.618033988749895
# @lc code=end

# class Solution:
    # def climbStairs(self, n: int) -> int:
    #     memo = [0] * (n + 1)
    #     return self.climb(n, memo)
    
    # def climb(self, n: int, memo: list[int]) -> int:
    #     if n <= 2:
    #         return n
    #     if memo[n] > 0:
    #         return memo[n]
    #     memo[n] = self.climb(n - 1, memo) + self.climb(n - 2, memo)
        
    #     return memo[n]

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one, two = 1, 1
#         for i in range(n):
#             two, one = one + two, two
#         return one
z = int(input())
s = perf_counter()
for i in range(z):
    start_time = perf_counter()

    m = Solution()
    print(m.climbStairs(i))

    end_time = perf_counter()
    print(f'Execution time: {(end_time - start_time)*1000} seconds')

end = perf_counter()
print(f'Execution time: {(end - s)*1000, end - s} seconds')
print(perf_counter())
print(perf_counter())
