from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        path = [[0,0]] + list(path)
        print(path[i-1][0])
        for i in range(1, len(path)):
            print(path)
            match path[i]:
                case "N": path[i] = [path[i-1][0] + 1, path[i-1][1]]
                case "S": path[i] = [path[i-1][0] - 1, path[i-1][1]]
                case "E": path[i] = [path[i-1][1], path[i-1][1] + 1]
                case "W": path[i] = [path[i-1][1], path[i-1][1] - 1]

            # if [x, y] in path: return True 
        print(path)

        return False  
                    
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.isPathCrossing("NESWW"))
# print(call)
print(t.hisobla(time, 1))



