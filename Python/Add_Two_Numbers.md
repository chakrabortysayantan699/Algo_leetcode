## Solution 1(Accepted)
```python 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        p = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry = l1.val + carry
                l1 = l1.next
            if l2:
                carry = l2.val + carry
                l2 = l2.next
            if carry >= 10:
                p.next = ListNode(carry - 10)
                carry = 1
            else:
                p.next = ListNode(carry)
                carry = 0
            p = p.next
        return dummy.next
       
```
## Solution 2(correct but rejected for using len() method
```python
# Definition for singly-linked list.
#class ListNode:
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next
class nodes:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Solution:
    def addTwoNumbers(self, l1, l2) :        
        self.head=None

        def printValues(L):
            a=''
            b=''
            temp=self.head
            while(temp):
                if(L==l1):
                    a+=str(temp.data)
                else:
                    b+=str(temp.data)
                temp=temp.next
            if(L==l1):
                return(int(a[: :-1]))
            return(int(b[: :-1]))
        
        L1=[l1,l2]
        for j in L1:
            for i in range(len(j)):
                if(i==0):
                    first_n=nodes(j[i])
                    self.head=first_n
                    old_node=first_n
                else:
                    new_node=nodes(j[i])
                    old_node.next=new_node
                    old_node=new_node
            ans1=printValues(j)
            if(j==l1):
                ans2=ans1
        #print(ans1+ans2)       
        return (ans1+ans2)
        
                    
#sol=Solution()
#l1=[1,7,3,4]
#l2=[5,9,7,8]                  
#sol.addTwoNumbers(l1,l2)

```
                
                
        
        
    
