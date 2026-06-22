# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        curr=slow
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        left=head
        right=prev

        while right:
            if right.val!=left.val:
                return False
            right=right.next
            left=left.next
        return True
