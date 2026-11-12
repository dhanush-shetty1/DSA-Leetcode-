# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        a1=[]
        a2=[]
        
        def recu(node):
            nonlocal a1
            if node is None:
                return 
            
            if node.left is None and node.right is None:
                a1.append(node.val)
            
            recu(node.left)
            recu(node.right)
        
        def recur(node):
            nonlocal a2
            if node is None:
                return 
            
            if node.left is None and node.right is None:
                a2.append(node.val)
            
            recur(node.left)
            recur(node.right)

        recu(root1)
        recur(root2)

        return a1==a2


        