# Solution 1 

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #def __init__(self):
        #self.head=None 
        
    def reverseList(self, head):  
        if head is None:
            return head
        prev= None
        cur=head
        while(cur is not None):
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        return prev
```
**Runtime: 47 ms, faster than 12.98% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 99.40% of Python3 online submissions for Reverse Linked List.**
            
        
        
