# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if not head:
        #     return

        # stack = []

        # curr = head
        # while curr:
        #     stack.append(curr)
        #     curr = curr.next

        # curr = head

        # # Number of reorder operations needed
        # for _ in range(len(stack) // 2):

        #     back = stack.pop()
        #     frontNext = curr.next

        #     curr.next = back
        #     back.next = frontNext

        #     curr = frontNext

        # # End the list
        # curr.next = None
        
        #find middle
        slow ,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse econd half
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge two halfs
        first, second = head, prev
        while second:
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
