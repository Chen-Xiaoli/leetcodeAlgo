# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head
        
        subHead = self.swapPairs(head.next.next)

        headNext = head.next

        headNext.next = head
        head.next = subHead

        return headNext







        