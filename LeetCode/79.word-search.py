from TestTime import TimeSet
from typing import List
from collections import defaultdict
from collections import Counter
t = TimeSet()

# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (40.63%)
# Likes:    14391
# Dislikes: 585
# Total Accepted:    1.4M
# Total Submissions: 3.3M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# Example 1:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# 
# 
# 
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
# 
#

# @lc code=start
# class Solution:
#     def exist(self, board, word: str) -> bool:
#         char = word[0]

#         def helper(col, row):
#             for i in [1, -1]:
#                 if 

        
#         l = len(board[0])
        
#         for row in range(len(board)):
#             for col in range(l):
#                 if char == board[row][col]:
#                     helper(col, row)

#         return False
    

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_r, len_c = len(board), len(board[0])

        if len(word) > len_r * len_c: return False
            
        count = Counter(sum(board, []))

        for c, countWord in Counter(word).items():
            if count[c] < countWord: return False
                
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        memo = set()

        def engine(r, c, i):
            if i == len(word): return True
            if r < 0 or c < 0 or r >= len_r or c >= len_c or word[i] != board[r][c] or (r, c) in memo:
                return False

            memo.add((r, c))
            res = (
                engine(r+1, c, i+1) or
                engine(r-1, c, i+1) or
                engine(r, c+1, i+1) or
                engine(r, c-1, i+1)
            )
            memo.remove((r, c))  # backtracking

            return res

        for row in range(len_r):
            for col in range(len_c):
                if engine(row, col, 0):
                    return True
                
        return False

# @lc code=end




time = t.hisobla()

m = Solution()
print(m.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"],["A","D","E","E"]], 'ABCCED'))

print(t.hisobla(time, 1))
