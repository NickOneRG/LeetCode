import heapq
from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2642 lang=python3
#
# [2642] Design Graph With Shortest Path Calculator
#

# @lc code=start
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj_list = {i: [] for i in range(n)}
        for edge in edges:
            self.adj_list[edge[0]].append((edge[1], edge[2]))

    def addEdge(self, edge: List[int]) -> None:
        self.adj_list[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        dist = {i: float('inf') for i in range(len(self.adj_list))}
        dist[node1] = 0

        while heap:
            (d, node) = heapq.heappop(heap)
            if node == node2:
                return d
            if d > dist[node]:
                continue

            for neighbor, weight in self.adj_list[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        return -1

        
# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
# @lc code=end
n     = 4
edges = [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]],[3, 2], [0, 3], [[1, 3, 4]], [0, 3]]

m = Graph(n, edges)
time = t.hisobla()
m.addEdge(edges)
print(m.shortestPath(2,3))
# print(call)
print(t.hisobla(time, 1))
