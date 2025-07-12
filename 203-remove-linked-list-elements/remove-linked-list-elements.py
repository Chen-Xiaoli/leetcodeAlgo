# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        cur = head

        while cur != None:
            if cur.val == val:
                pre.next = cur.next
                cur = pre.next
            else:
                cur = cur.next
                pre = pre.next

        return dummy.next