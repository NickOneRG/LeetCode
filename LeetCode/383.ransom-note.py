#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = 0
        z = 0
        li = []
        for i in magazine:
            li.append(i)
        while True:
            if ransomNote[z] in li:
                li.remove(ransomNote[z])
                s += 1
                if len(ransomNote) == s:
                    return True
           
            else:
                return False
            z += 1
            
# @lc code=end

m = Solution()
print(m.canConstruct(input(), input()))