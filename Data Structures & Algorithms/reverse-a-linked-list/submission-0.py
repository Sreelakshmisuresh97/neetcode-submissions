# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev = None
        curr = head
        #next1 = head.next
        while curr!=None:
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1
            
        head = prev
        return head        