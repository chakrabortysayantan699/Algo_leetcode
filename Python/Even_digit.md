# Solution 1

``` python

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even=0
        for i in nums:
            ob= str(i)
            n=(len(ob) %2)
            if(n==0):
                even+=1
        return even
        
```
