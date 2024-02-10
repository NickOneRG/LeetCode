from itertools import combinations
from TestTime import TimeSet
from typing import List
from math import ceil
t = TimeSet()
#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start


class Solution:
    def countSubstrings(self, s: str) -> int:

        return sum(1 for x, y in combinations(range(len(s) + 1), r=2) if (pal := s[x:y]) == pal[::-1])


class Solution:
    def countSubstrings(self, s: str) -> int:
        def f(l, r):
            while l > -1 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return ceil((r-l-1)/2)
        
        res, n = 0, len(s)

        for i in range(n):
            res += f(i, i)

            if i < n-1: res += f(i, i+1)
                
        return res
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.countSubstrings("abc"))
# print(call)
print(t.hisobla(time, 1))

# def count_substrings(input_string):
#     return sum(len(input_string) - i for i in range(len(input_string)))

# my_string = "aaa"
# num_substrings = count_substrings(my_string)
# print(f"Number of substrings in '{my_string}': {num_substrings}")


# def get_all_substrings(input_string):
#     if len(input_string) == 0:
#         return []
#     elif len(input_string) == 1:
#         return [input_string]
#     else:
#         output = []
#         for i in range(len(input_string)):
#             for j in range(i + 1, len(input_string) + 1):
#                 output.append(input_string[i:j])
#         return output + get_all_substrings(input_string[1:])


# my_string = "aaa"
# substrings = get_all_substrings(my_string)
# print(substrings)


# input_string = "aaa"
# substrings = [pal for x, y in combinations(range(len(input_string) + 1), r=2) if (pal := input_string[x:y]) == pal[::-1]]


# print(substrings)
