#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
            
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A: target[x] += 1
            
        l = len(A)
        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= l:
                window[B[i - l]] -= 1
            if window == target:
                return True
            
        return False
        
# @lc code=end

m = Solution()
print(m.checkInclusion("ab", "eidbaooo"))
