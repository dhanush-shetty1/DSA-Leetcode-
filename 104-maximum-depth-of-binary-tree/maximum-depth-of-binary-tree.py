# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def solve(node):
            if node is None:
                return 0

            L=solve(node.left)
            R=solve(node.right)

            return 1+max(L,R)
        
        return solve(root)