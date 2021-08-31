# Solution 1

``` python
# DFS
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.dfs(root, None)
        return root

    def dfs(self, root, cur_next):
        if root is None:
            return
        root.next = cur_next
        self.dfs(root.left, root.right)
        if root.next is None:
            self.dfs(root.right, None)
        else:
            self.dfs(root.right, root.next.left)
            
```
