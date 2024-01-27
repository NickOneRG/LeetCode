#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets) -> [str]:
        li = []
        tek = []
        b = 1

        for z in list(tickets):
            if b > 0:
                li.append(z[0])
                li.append(z[1])
                b = 0
                # tek = z
            
            elif z[1] == tek[0]:
                li.insert(len(li)-2, z[0])
                li.insert(len(li)-2, z[1])
            elif z[0] == li[len(li)-1]:
                li.append(z[0])
                li.append(z[1])
            else:
                li.append(z[0])
                li.append(z[1])
            print(li)
            tek = z
        li = set(li)
        return li
            
# @lc code=end

m = Solution()
li = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# li = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(m.findItinerary(li))