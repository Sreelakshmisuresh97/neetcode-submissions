# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head3=prev3= ListNode()
        carry = 0
        while l1 or l2:
            
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            num = num1 + num2+carry
            
            if num > 9:
                carry = 1
                num = num%10
                print(num)
            else:
                carry =0
            l3 = ListNode(num)
            prev3.next =l3
            prev3 = l3
            l1 = l1.next if l1 else l1
            l2= l2.next if l2 else l2
        if carry:
            l3 = ListNode(1)
            prev3.next = l3   
        return head3.next     
              
        