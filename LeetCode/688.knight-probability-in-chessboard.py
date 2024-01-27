from TestTime import TimeSet
from typing import List
t = TimeSet()
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#

# @lc code=start
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                 (1, -2), (1, 2), (2, -1), (2, 1)]

        cur_board = [[0.0] * n for _ in range(n)]
        next_board = [[0.0] * n for _ in range(n)]
        next_board[row][column] = 1.0

        for _ in range(k):
            cur_board, next_board = next_board, [[0.0] * n for _ in range(n)]

            for r in range(n):
                for c in range(n):
                    if cur_board[r][c] == 0.0:
                        continue

                    for dr, dc in moves:
                        next_row, next_col = r + dr, c + dc

                        if 0 <= next_row < n and 0 <= next_col < n:
                            next_board[next_row][next_col] += cur_board[r][c] / 8.0

        total = 0.0
        for r in range(n):
            for c in range(n):
                total += next_board[r][c]

        return total


# @lc code=end


m = Solution()
time = t.hisobla()
print(m.knightProbability(3, 2, 0, 0))
print(t.hisobla(time, 1))
