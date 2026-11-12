# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        a1=[]
        a2=[]

        def check(node,arr):
            qu=deque([node])

            while len(qu)!=0:
                e=qu.popleft()
                if e is None:
                    arr.append(None)
                    continue
                arr.append(e.val)

                qu.append(e.left)
                qu.append(e.right)
        
        check(p,a1)
        check(q,a2)

        return a1==a2

        

        