# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        for i in range(len(lists)):
            cur = lists[i]
            while cur:
                heapq.heappush(pq, (cur.val))
                cur = cur.next
           
        
        dummy = ListNode(-1)
        
        cur = dummy

        while pq:
            cur.next = ListNode(heapq.heappop(pq))
            cur = cur.next
        return dummy.next
        

         