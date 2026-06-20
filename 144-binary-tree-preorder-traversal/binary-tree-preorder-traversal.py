# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre(self,root):
        if root is None:
            return
        self.arr.append(root.val)
        self.pre(root.left)
        self.pre(root.right)


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.arr=[]
        self.pre(root)
        return self.arr
        