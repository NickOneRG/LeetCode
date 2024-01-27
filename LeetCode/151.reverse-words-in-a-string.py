#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        li = []
        for i in s:
            l = ''
            n = 1
            while n == 1:
                if i == " ":
                    n = 0
                if i.isalpha:
                    l+=(i)
                    
        li.append(l)      
                
        return l[::-1]
# @lc code=end

m = Solution()
print(m.reverseWords("a good   example"))