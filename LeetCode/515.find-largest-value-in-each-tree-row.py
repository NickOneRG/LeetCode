from TestTime import TimeSet
from typing import Optional, List
t = TimeSet()
#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.

class Solution:
    def largestValues(self, root):
        if not root: return []

        memo, res = [(root,0)], defaultdict(lambda : float("-inf"))

        while memo:
            node, count = memo.pop(0)
            res[count]  = max(res[count],node.val)
            if node.left:  memo.append((node.left,count+1))
            if node.right: memo.append((node.right,count+1))

        return res.values()

# @lc code=end

m = Solution()
time = t.hisobla()
print(m.largestValues([1,3,2,5,3,None,9,5]))
# print(call)  
print(t.hisobla(time,1))
