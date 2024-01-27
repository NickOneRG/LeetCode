#
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
class Solution:
    def exist(self, board, word: str) -> bool:
        a = board[0]
        b = board[1]
        c = board[2]
        g = ''
        for z in range(len(word)):
            if word[z] in a:
                for i in range(len(a)):
                    if word[z] == a[i]:
                        print(a[i])
                        

            elif word[z] in b:
                pass
            elif word[z] in c:
                pass
            else:
                return False

        
        
        return(a,b,c)
# @lc code=end


m = Solution()
s = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"],["A","D","E","E"]]
print(m.exist(s, 'ABCCED'))
