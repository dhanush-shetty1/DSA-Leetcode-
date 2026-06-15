# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        n = count // 2 - 1

        curr = head
        for _ in range(n):
            curr = curr.next

        curr.next = curr.next.next

        return head