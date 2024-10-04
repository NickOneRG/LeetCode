#
# @lc app=leetcode id=2490 lang=python3
#
# [2490] Circular Sentence
#

# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()

        if sentence[0][0] != sentence[-1][-1]: return False
            
        for i in range(len(sentence)-1):
            if sentence[i][-1] != sentence[i+1][0]: return False
        
        return True
# @lc code=end


m = Solution()
print(m.isCircularSentence("Leetcodel"))
