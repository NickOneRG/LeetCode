from collections import Counter
import bisect
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         word = Counter(word2)
#         count = list(word.values())
#         word = word.keys()

#         for k, v in Counter(word1).items():

#             if k not in word or v not in count: 
#                 return False
#             else: count.remove(v)

#         return True and len(word1) == len(word2)
# # @lc code=end


# m = Solution()
# time = t.hisobla()
# print(m.closeStrings("abbzzca", "babzzcz"))
# # print(call)
# print(t.hisobla(time, 1))

# class Solution:
#     def findMaximumNumber(self, k: int, x: int) -> int:
#         left, right = 0, 343778878348159
#         val = 1 << x - 1
#         val_1 = 1 << x
#         while left <= right:
#             num, tmp = (left + right) // 2, val
#             res = 0

#             while tmp <= num:
#                 x, y = divmod(num, 2 * tmp)
#                 res += x * tmp + max(0, y - tmp + 1)
#                 tmp *= val_1

#             if res > k: right = num - 1
#             else: left = num + 1
                
#         return right



# m = Solution()
# time = t.hisobla()
# print(m.findMaximumNumber(7,2))
# # print(call)
# print(t.hisobla(time, 1))


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def f(p):
            memo = [0] * (l_p := len(p))
            j = 0
            for i in range(1, l_p):
                while j != 0 and p[j] != p[i]:
                    j = memo[j - 1]
                if p[j] == p[i]: j += 1
                    
                memo[i] = j
            return memo

        f_a = f(a + '#' + s)
        f_b = f(b + '#' + s)

        len_a, len_b = len(a), len(b)

        b_ind, res = [i - len_b * 2 for i in range(len(f_b)) if f_b[i] == len_b], []
        len_bind = len(b_ind)

        for i in [i - len_a * 2 for i in range(len(f_a)) if f_a[i] == len_a]:
            p = bisect.bisect(b_ind, i)

            for p1 in range(p - 1, p + 2):
                if 0 <= p1 < len_bind and abs(b_ind[p1] - i) <= k:
                    res.append(i)
                    break
        return res


m = Solution()
time = t.hisobla()
print(m.beautifulIndices(  "isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15))
# print(call)
print(t.hisobla(time, 1))


def countingSort(arr):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        count[arr[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print(data)

               

