# solution 1

```python

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new=[]
        first=nums[:n]
        second=nums[n:]
        for i in range(len(first)):
            new.append(first[i])
            new.append(second[i])
        return new
        
```

        
