from collections import defaultdict
from bisect import bisect_left, bisect_right
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#

# @lc code=start
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        def_d = defaultdict(list)
        for i, c in enumerate(s): def_d[c].append(i)
        
        for c, i in def_d.items():
            l = len(i)
            if l < 2: continue
            if l > 2: res += 1

            for k, j in def_d.items():
                if c == k: continue
                if bisect_left(j, i[0]) < bisect_left(j, i[-1]): res += 1
                    
        return res

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.countPalindromicSubsequence("bbcbaba"))
# print(call)  
print(t.hisobla(time,1))

# def printSub(arr, index, subarr): 
#     if index == len(arr):
#         if len(subarr) == 3 and subarr == subarr[::-1]:
#             print(subarr)
#         return
#     else:
#         printSub(arr, index + 1, subarr)
#         printSub(arr, index + 1, subarr+[arr[index]])


# arr = list("bbcbabablcjhfghxjklkjhv")
# printSub(arr, 0, [])

# class Solution:
#     def countPalindromicSubsequence(self, inputString):
#         min_exist = [float('inf')] * 26
#         max_exist = [float('-inf')] * 26

#         for i in range(len(inputString)):
#             char_index = ord(inputString[i]) - ord('a')
#             min_exist[char_index] = min(min_exist[char_index], i)
#             max_exist[char_index] = max(max_exist[char_index], i)

#         unique_count = 0

#         for char_index in range(26):
#             if min_exist[char_index] == float('inf') or max_exist[char_index] == float('-inf'):
#                 continue  

#             unique_chars_between = set()

#             for j in range(min_exist[char_index] + 1, max_exist[char_index]):
#                 unique_chars_between.add(inputString[j])

#             unique_count += len(unique_chars_between)

#         return unique_count
    
