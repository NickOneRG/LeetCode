#
# @lc app=leetcode id=1458 lang=python3
#
# [1458] Max Dot Product of Two Subsequences
#

# @lc code=start
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N1, N2 = len(nums1), len(nums2)
        INF = 10 ** 20

        d_p = [[-INF] * N2 for _ in range(N1)]
        p = [[nums1[i] * nums2[j] for j in range(N2)] for i in range(N1)]

        for i in range(N1):
            for j in range(N2):
                if i == 0 and j == 0:
                    d_p[i][j] = p[i][j]
                elif i == 0:
                    d_p[i][j] = max(p[i][j], d_p[i][j - 1])
                elif j == 0:
                    d_p[i][j] = max(p[i][j], d_p[i - 1][j])
                else:
                    d_p[i][j] = max(d_p[i - 1][j - 1] + p[i][j],
                                    d_p[i - 1][j], d_p[i][j - 1])
                if i > 0 and j > 0:
                    d_p[i][j] = max(d_p[i][j], d_p[i - 1][j - 1] + p[i][j])

        return d_p[N1 - 1][N2 - 1]
        
# @lc code=end

