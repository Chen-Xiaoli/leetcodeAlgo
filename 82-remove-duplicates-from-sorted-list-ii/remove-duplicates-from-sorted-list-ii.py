# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        dummy = ListNode()
        dummy.next = head
        
        last = dummy
        pre = head
        cur = head.next

        while cur:
            if pre.val == cur.val:
                while cur and pre.val == cur.val:
                    cur = cur.next
                last.next = cur
                pre = cur
                if cur:
                    cur = cur.next 
            else:
                pre = pre.next
                cur = cur.next
                last = last.next

        return dummy.next
            
       
               
           


