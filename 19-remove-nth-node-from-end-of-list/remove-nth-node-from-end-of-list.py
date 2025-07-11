# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        latter = dummy
        cur = head
        former = head

        for i in range(n):
            former = former.next
        
        while former != None:
            former = former.next
            latter = cur
            cur = cur.next
        latter.next = cur.next

        return dummy.next


        