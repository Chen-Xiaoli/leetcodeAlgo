# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        point = math.ceil((count + 1)/2)

        print(point)

        temp = head
        count = 1 
        while count != point:
            count += 1
            temp = temp.next
        return temp

        