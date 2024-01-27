from collections import Counter
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        memo = Counter(chars)

        for word in words:
            memo, count = chars, 0
            
            for char in word:
                if memo[char] > 0:
                    memo[char] -= 1
                    count += 1
                else: break
            else: continue
            # if count == len(word):
            res += count

        return res

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
print(t.hisobla(time, 1))



class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res, chars_c = 0, Counter(chars)

        for word in words:
            word_c = Counter(word)

            for char in word_c:
                if word_c[char] > chars_c[char]: break
                    
            else: res += len(word)

        return res