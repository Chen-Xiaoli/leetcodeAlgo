# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        
        # Initialize heap with the first node of each non-empty list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(pq, (node.val, i, node))
        
        dummy = ListNode(-1)
        cur = dummy
        
        while pq:
            val, i, node = heapq.heappop(pq)
            cur.next = node
            cur = cur.next
            
            # If the popped node has a next node, add it to heap
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
                
        return dummy.next
        

         