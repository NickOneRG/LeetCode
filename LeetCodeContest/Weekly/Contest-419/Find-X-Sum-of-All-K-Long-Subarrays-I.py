

MOD = 10**9 + 7


class Solution:
    def countWinningSequences(self, s: str) -> int:
        n = len(s)
        win_against = {'F': 'W', 'W': 'E', 'E': 'F'}

        memo = {}

        def dp(i, last_bob_move, score_diff):
            if i == n:
                return 1 if score_diff > 0 else 0

            if (i, last_bob_move, score_diff) in memo:
                return memo[(i, last_bob_move, score_diff)]

            total_ways = 0
            alice_move = s[i]

            for bob_move in 'FWE':
                if bob_move == last_bob_move:
                    continue

                new_score_diff = score_diff
                if bob_move == win_against[alice_move]:
                    new_score_diff += 1
                elif win_against[bob_move] == alice_move:
                    new_score_diff -= 1

                total_ways = (
                    total_ways + dp(i + 1, bob_move, new_score_diff)) % MOD

            memo[(i, last_bob_move, score_diff)] = total_ways
            return total_ways

        return dp(0, None, 0)



m = Solution()
print(m.countWinningSequences("FWEFW"))
