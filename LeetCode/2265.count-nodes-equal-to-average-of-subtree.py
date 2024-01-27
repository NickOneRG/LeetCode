#
# @lc app=leetcode id=2265 lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
#

# @lc code=start
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def count(root):
            nonlocal res
            if not root: return (0,0)
            l = count(root.left)
            r = count(root.right)

            if (root.val + l[1] + r[1]) // (1 + l[0] + r[0]) == root.val: res += 1
                
            return (1 + l[0] + r[0], root.val + l[1] + r[1])
        count(root)
        return res
        
# @lc code=end

