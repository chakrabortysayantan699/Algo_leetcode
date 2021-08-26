# Solution 1

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) :
        
        dummy = ListNode(-1)
        dummy.next = head
        p, q = dummy, dummy
        
        for _ in range(n):            
            p = p.next
        
        while p.next:
            p = p.next
            q = q.next
            
        q.next = q.next.next
        return dummy.next
```
