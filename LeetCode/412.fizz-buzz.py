from typing import List
#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i) for i in range(1, n+1)]
        for i in range(1, n+1):
            if i % 5 == 0:
                res[i-1] = "FizzBuzz" if i % 3 == 0 else "Buzz"
            elif i % 3 == 0:
                res[i-1] = "Fizz"
            
        return res



# @lc code=end

m = Solution()
print(m.fizzBuzz(15))