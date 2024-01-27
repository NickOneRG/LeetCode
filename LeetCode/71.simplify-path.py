from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []

        for i in path.split("/"):
            if res and i == "..":          res.pop()
            elif i not in [".", "", ".."]: res.append(i)
                
        return "/" + "/".join(res)


# @lc code=end

m = Solution()
time = t.hisobla()
print(m.simplifyPath("/home/"))
# print(call)  
print(t.hisobla(time,1))
print(t.rav())
