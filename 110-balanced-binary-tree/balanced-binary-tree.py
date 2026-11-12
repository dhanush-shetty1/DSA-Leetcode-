# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        flag=True
        def check(node):
            nonlocal flag
            if node is None:
                return 0

            L=check(node.left)
            R=check(node.right)
            if abs(L-R)>1:
                flag=False
            return 1+max(L,R)

        check(root)
        return flag