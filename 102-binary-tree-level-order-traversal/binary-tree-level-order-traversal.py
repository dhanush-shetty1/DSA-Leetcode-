from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res=[]
        queue=deque([root])

        while queue:
            t=[]
            level=len(queue)
            for i in range(level):
                e=queue.popleft()
                t.append(e.val)

                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            res.append(t)
                
        
        return res
        
        