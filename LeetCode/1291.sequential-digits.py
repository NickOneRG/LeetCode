from TestTime import TimeSet
from typing import List
from collections import Counter
t = TimeSet()
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#

# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        l = len(str(low))
        count = int(str(low)[0])-1

        while True:
            memo = ""
            for i in range(1, l+1):
                memo += str(i+count)
            
            if i+count == 9:
                l += 1
                count = 0
            else: count += 1

            memo = int(memo)
            if memo > high: break

            if memo > low:
                res.append(memo)

        return res


        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.sequentialDigits(58, 155))
# print(call)
print(t.hisobla(time, 1))

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0] * len(s)

        for val, ind in zip(s, indices):
            res[ind] = val

        def generator():
            for val in res:
                yield val
        print(*generator())
        return "".join(generator())

m = Solution()
time = t.hisobla()
print(m.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
# print(call)
print(t.hisobla(time, 1))
