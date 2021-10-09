# solution 1

```python

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(set(nums))
        p=len(nums)
        if(n!=p):
            return True
        else:
            return False
        
```
