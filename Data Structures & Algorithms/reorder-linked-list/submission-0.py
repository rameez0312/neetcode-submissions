# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        stack = []

        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head

        # Number of reorder operations needed
        for _ in range(len(stack) // 2):

            back = stack.pop()
            frontNext = curr.next

            curr.next = back
            back.next = frontNext

            curr = frontNext

        # End the list
        curr.next = None
        