from collections import defaultdict, deque
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=815 lang=python3
#
# [815] Bus Routes
#

# @lc code=start
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target: return 0
    
        max_stop = max(max(route) for route in routes)
        if max_stop < target: return -1

        min_to_r = [float('inf')] * (max_stop + 1)
        min_to_r[source] = 0

        flag = True
        while flag:
            flag = False
            for route in routes:
                mini = float('inf')
                for stop in route:
                    mini = min(mini, min_to_r[stop])
                mini += 1
                for stop in route:
                    if  min_to_r[stop] > mini:
                        min_to_r[stop] = mini
                        flag = True
        return min_to_r[target] if min_to_r[target] < float('inf') else -1


# @lc code=end


m = Solution()
time = t.hisobla()
print(m.numBusesToDestination(
    [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 15))
# print(call)  
print(t.hisobla(time,1))




class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0

        def_d = defaultdict(set)
        for i, route in enumerate(routes):
            for node in route: def_d[node].add(i)
                
        res, vis = -1, set()
         
        queue = deque()
        queue.append(source)
        while queue:
            l = len(queue)
            res += 1
            for _ in range(l):
                cur = queue.popleft()
                if cur == target:
                    return res
                for bus in def_d[cur]:
                    if bus not in vis:
                        vis.add(bus)
                        queue.extend(routes[bus])
        return -1