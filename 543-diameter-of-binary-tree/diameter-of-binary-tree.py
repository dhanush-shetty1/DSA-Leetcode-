# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        self.solve(root)
        return self.diameter

    def solve(self,node):
        if node==None:
            return 0
            
        L=self.solve(node.left)
        R=self.solve(node.right)
        self.diameter=max(self.diameter, L+R)
        return 1+max(L,R)

        
       
        

        