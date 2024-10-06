import copy
from typing import List
#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isgood(board, row, col, i):
            for j in board[row]:
                if j == str(i):
                    return False

            for j in range(9):
                if board[j][col] == str(i):
                    return False

            r = (row // 3) * 3
            c = (col // 3) * 3

            for a in range(r, r + 3):
                for b in range(c, c + 3):
                    if board[a][b] == str(i):
                        return False

            return True

        dot = 0
        for line in board:
            for i in line:
                if i == ".":
                    dot += 1

        def f(board, row, col):

            if row == 9:
                return True

            nextrow = row
            nextcol = col

            if col == 9:
                return f(board, row + 1, 0)

            if board[row][col] != ".":
                return f(board, row, col + 1)

            for i in range(1, 10):
                if isgood(board, row, col, i):
                    board[row][col] = str(i)
                    if f(board, nextrow, nextcol):
                        return True
                    else:
                        board[row][col] = "."

        f(board, 0, 0)
        # for i in board:
        #     print(i)




# @lc code=end

m = Solution()
print(m.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], 
                     ["6", ".", ".", "1", "9", "5", ".", ".", "."], 
                     [".", "9", "8", ".", ".", ".", ".", "6", "."], 
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
                     [".", "6", ".", ".", ".", ".", "2", "8", "."], 
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))


# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """

#         def f_plus(row, col, num):
#             a, b = 0, 0
#             for i in range(9):
#                 if board[i][col] == '.' and num in  board[i]:
#                     a += 1
#             for i in range(9):
#                 if board[row][i] == '.':
#                     for j in range(9):
#                         if board[j][i] == num:
#                             b += 1
#             print(num, a, b)
            
#             return a*b



#         def f(row, col):
#             vertical = []
#             for i in range(9):
#                 if (b := board[i][col]) != '.':
#                     vertical.append(b)

#             box = []
#             r = 3 * (row // 3)
#             c = 3 * (col // 3)
#             for i in range(3):
#                 for j in range(3):
#                     if (b := board[i+r][j+c]) != '.':
#                         box.append(b)
#             # print(box)

#             memo = []
#             for i in range(1, 10):
#                 i = str(i)
#                 if i not in board[row] and i not in vertical and i not in box:
#                     memo.append(i)
#             # print(memo)

#             res = [0, 0]
#             for i in memo:
#                 c = f_plus(row, col, i)
#                 if c > res[1]:
#                     res[1] = c
#                     res[0] = i 
#             return res[0]
        

#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] == ".":
#                     board[i][j] = f(i, j)
        
#         for i in board:
#             print(i)



# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         possible = [[
#             {x: None for x in "123456789"} for _ in range(9)
#         ] for _ in range(9)]

#         missing = 0
#         to_explore = []

#         def delete(char, i, j, possible):
#             sq_row_inds = i // 3 * 3, i // 3 * 3 + 3
#             sq_col_inds = j // 3 * 3, j // 3 * 3 + 3
#             deleted = []
#             for k in range(9):
#                 if char in possible[k][j]:
#                     del possible[k][j][char]
#                     deleted.append((k, j))
#                 if char in possible[i][k]:
#                     del possible[i][k][char]
#                     deleted.append((i, k))
#             for k1 in range(sq_row_inds[0], sq_row_inds[1]):
#                 for k2 in range(sq_col_inds[0], sq_col_inds[1]):
#                     if char in possible[k1][k2]:
#                         del possible[k1][k2][char]
#                         deleted.append((k1, k2))
#             return deleted

#         for i in range(9):
#             for j in range(9):
#                 char = board[i][j]
#                 if char == '.':
#                     missing += 1
#                     to_explore.append((i, j))
#                 else:
#                     delete(char, i, j, possible)

#         def restore(char, possible, deleted):
#             for di, dj in deleted:
#                 possible[di][dj][char] = None

#         def dfs(possible, to_explore, track):
#             if not to_explore:
#                 return True

#             to_explore.sort(key=lambda x: -len(possible[x[0]][x[1]]))

#             i, j = to_explore[-1]
#             poss = possible[i][j]
#             if not poss:
#                 return False

#             for char in poss.copy():
#                 to_explore.pop()
#                 board[i][j] = char
#                 deleted = delete(char, i, j, possible)
#                 track.append((i, j, char))
#                 result = dfs(possible, to_explore, track)
#                 if result:
#                     return True

#                 track.pop()

#                 board[i][j] = '.'
#                 restore(char, possible, deleted)
#                 to_explore.append((i, j))
                
#             return False
            
#         dfs(possible, to_explore, [])
#         # for i in board:
#         #     print(i)