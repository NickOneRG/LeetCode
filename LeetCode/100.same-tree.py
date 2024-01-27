#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSameTree(self, p, q ) -> bool:
        # return True if p == q else False
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def isSameTree(p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# @lc code=end

m = Solution()
p = [1,2,3]
q = [1,2,3]
print(m.isSameTree(p, q))
