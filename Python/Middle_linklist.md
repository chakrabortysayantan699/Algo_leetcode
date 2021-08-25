# Solution 1

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        # with two pointer method 1.First 2.second
        First=Second=head
        while First and First.next:
            Second=Second.next
            First=First.next.next
        return(Second)
```
[Two Pointer Method  with Picture (Fast,Slow)](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20201117195251/middle-of-a-given-linked-list-in-C-and-Java1.png)
        
