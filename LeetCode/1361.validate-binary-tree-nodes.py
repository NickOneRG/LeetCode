from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1361 lang=python3
#
# [1361] Validate Binary Tree Nodes
#

# @lc code=start
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root, children = 0, set(leftChild + rightChild)
    
        for i in range(n):
                if i not in children: root = i

        check, num, memo  = [False] * n, 0, [root]
        while memo:
            curr = memo.pop(0)
            if check[curr]: return False
                
            check[curr] = True

            left, right = leftChild[curr], rightChild[curr]
            if left  != -1: memo.append(left)
            if right != -1: memo.append(right)
            num += 1
                
        return num == n
# @lc code=end

m = Solution()
time = t.hisobla()
# for i in range(25000):
#      m.validateBinaryTreeNodes(4,[3,-1,1,-1],[-1,-1,0,-1])
print(m.validateBinaryTreeNodes(4,[3,-1,1,-1],[-1,-1,0,-1]))
# print(call)  
print(t.hisobla(time,1))