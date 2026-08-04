# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            # Find kth node
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            # Reverse current group
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Connect reversed group
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp