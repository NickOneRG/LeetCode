from typing import Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.sizes = []
    
    def isPerfect(self, root):
        if not root:
            return True, 0

        left_perfect, left_size = self.isPerfect(root.left)
        right_perfect, right_size = self.isPerfect(root.right)

        if left_perfect and right_perfect and left_size == right_size:
            size = 1 + left_size + right_size
            self.sizes.append(size)
            return True, size
        
        return False, 0

    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        self.isPerfect(root)
        self.sizes.sort(reverse=True)
        if len(self.sizes) >= k:
            return self.sizes[k - 1]
        return -1
    


