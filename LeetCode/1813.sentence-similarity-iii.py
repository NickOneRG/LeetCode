#
# @lc app=leetcode id=1813 lang=python3
#
# [1813] Sentence Similarity III
#

# @lc code=start
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()

        if len(s1) > len(s2):
            s1, s2 = s2, s1

        len_s1 = len(s1)

        def f(num):
            i, j = 0, 1
            if num == 1: j = 0
                
            while i < len_s1 and s1[(i+j) * num] == s2[(i+j) * num]:
                i += 1
            return i

        return f(1) + f(-1) >= len_s1

# @lc code=end

m = Solution()
print(m.areSentencesSimilar("of", "A lot of words"))
