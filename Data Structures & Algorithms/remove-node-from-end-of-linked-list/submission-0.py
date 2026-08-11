# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        fp , sp = dummy, head

        while n>0 and sp:
            sp = sp.next
            n = n-1
        
        
        while sp:
            sp = sp.next
            fp = fp.next
        
        fp.next = fp.next.next
        return dummy.next
