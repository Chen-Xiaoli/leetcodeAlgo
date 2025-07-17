# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        newHead =  ListNode(-1)
        dummy.next = newHead

        cur1 = l1
        cur2 = l2
        c = 0

        while cur1 and cur2:
            newNode =  ListNode(-1)
            if (cur1.val + cur2.val + c - 10) >= 0:
                newNode.val = cur1.val + cur2.val + c - 10 
                c = 1
            else:
                newNode.val = cur1.val + cur2.val + c
                c = 0
            newHead.next = newNode
            newHead = newHead.next

            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            newNode =  ListNode(-1)
            if cur1.val + c - 10 >= 0:
                newNode.val = cur1.val + c - 10 
                c = 1
            else:
                newNode.val = cur1.val + c
                c = 0
            newHead.next = newNode
            newHead = newHead.next

            cur1 = cur1.next

        while cur2:
            newNode =  ListNode(-1)
            if cur2.val + c - 10 >= 0:
                newNode.val = cur2.val + c - 10 
                c = 1
            else:
                newNode.val = cur2.val + c
                c = 0
            newHead.next = newNode
            newHead = newHead.next

            cur2 = cur2.next
       
        if c:
            newNode =  ListNode(-1)
            newNode.val = c
            newHead.next = newNode

        return dummy.next.next



            

        