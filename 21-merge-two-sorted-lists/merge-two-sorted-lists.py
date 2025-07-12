# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        dummy = ListNode(-1)
        insert = dummy
        
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                insert.next = cur1
                cur1 = cur1.next
                insert = insert.next
            else:
                insert.next = cur2
                cur2 = cur2.next
                insert = insert.next
        if cur1 != None:
            insert.next = cur1
        if cur2 != None:
            insert.next = cur2
        return dummy.next

        