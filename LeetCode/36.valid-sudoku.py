from typing import List
#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1, "8": 1, "9": 1, ".": 9}
        
        for i in range(9):
            memo = d.copy()
            for j in range(9):
                if memo[board[i][j]]:
                    memo[board[i][j]] -= 1
                else:
                    return False
            memo = d.copy()
            for j in range(9):
                if memo[board[j][i]]:
                    memo[board[j][i]] -= 1
                else:
                    return False

        row, col = 0, 0
        for i in range(9):
            memo = d.copy()
            for r in range(3):
                for c in range(3):
                    if memo[(m :=board[r+row][c+col])]:
                        memo[m] -= 1
                    else:
                        return False
                    
            row += 3
            if row == 9:
                row = 0
                col += 3
        return True
        
# @lc code=end

m = Solution()
print(m.isValidSudoku([[".", ".", ".", ".", ".", ".", "5", ".", "."], 
                       [".", ".", ".", ".", ".", ".", ".", ".", "."], 
                       [".", ".", ".", ".", ".", ".", ".", ".", "."], 
                       ["9", "3", ".", ".", "2", ".", "4", ".", "."], 
                       [".", ".", "7", ".", ".", ".", "3", ".", "."], 
                       [".", ".", ".", ".", ".", ".", ".", ".", "."], 
                       [".", ".", ".", "3", "4", ".", ".", ".", "."], 
                       [".", ".", ".", ".", ".", "6", ".", ".", "."], 
                       [".", ".", ".", ".", ".", "5", "2", ".", "."]]))

