# Solution 1

```python

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0,0)
        for i in range(len(gain)):
            if(i>=1):
                gain[i]+=gain[i-1]
                
        ans=max(gain)
        return ans
        
 ```
 
