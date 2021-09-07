# Solution 1

```python

class Solution:
    def reverseBits(self, n: int):
        ans, power = 0, 31
        while n:
            ans += (n & 1) << power
            n = n >> 1
            power -= 1
        return ans
        
```
