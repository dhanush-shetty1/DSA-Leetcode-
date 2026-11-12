# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        ans=float('-inf')
        def tsum(node):
            nonlocal ans

            if node is None:
                return 0

            l=tsum(node.left)
            if l<0:
                l=0
            r=tsum(node.right)
            if r<0:
                r=0
            ans=max(ans,node.val+l+r)
            return node.val + max(l,r)
        
        tsum(root)
        return ans
        