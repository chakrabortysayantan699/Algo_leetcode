# Solution 1

``` python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        c=[]
        for i in range(len(nums)):
            a=nums[i]**2
            c.append(a)
        c.sort()
        return c
```
