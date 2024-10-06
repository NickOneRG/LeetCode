from typing import List
#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        memo = {2: ['a', 'b', 'c'],
                3: ['d', 'e', 'c'],
                4: ['g', 'h', 'i'],
                5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'],
                7: ['p', 'q', 'r', 's'],
                8: ['t', 'u', 'v'],
                9: ['w', 'x', 'y', 'z']
                }
        
        def f(i):
            if digits[i] != digits[-1]:
                return f(i+1)
            else:
                pass
# @lc code=end

