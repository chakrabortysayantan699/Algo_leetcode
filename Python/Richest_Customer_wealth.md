# Solution 1

```python 

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        b=0
        ans=0
        for i in range(len(accounts)):
            for j in (accounts[i]):
                b+=j
            ans=max(b,ans)
            b=0
        return ans
```
