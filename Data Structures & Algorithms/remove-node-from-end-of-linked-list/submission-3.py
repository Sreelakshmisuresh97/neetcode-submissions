# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length+=1
            curr=curr.next
        n1 = length-n
    
        if n1==0:
            head = head.next
        else:
            curr = head
            print(n1)
            while n1>1:
                print("h")
                curr=curr.next
                n1-=1
            temp = curr.next.next
            curr.next= temp
        return head         
