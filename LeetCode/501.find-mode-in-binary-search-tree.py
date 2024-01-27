#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.leftright = right    
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts, nodes, max_count = {}, [], 0

        def inorder(node):
            if not node: return
            inorder(node.left)
            nonlocal max_count, nodes
            counts[node.val] = 1 + counts.get(node.val, 0)
            
            if counts[node.val] > max_count:    max_count, nodes = counts[node.val], [node.val]
            elif counts[node.val] == max_count: nodes.append(node.val)

            inorder(node.right)
        inorder(root)

        return nodes
        
# @lc code=end

