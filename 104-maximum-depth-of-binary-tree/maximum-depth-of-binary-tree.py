# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        ans=0
        queue=deque([root])

        while queue:
            for i in range(len(queue)):
                e=queue.popleft()
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            ans+=1
        
        return ans
        