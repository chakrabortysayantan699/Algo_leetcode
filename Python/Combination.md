# Soltuion 1(with inbuild fuction)

``` python
from itertools import combinations as comb
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if((1<=n<=20) and (1<=k<=n)):
            a=[]
            b=[]
            for i in range(1,n+1):
                a.append(i)
            combi=comb(a,k)
            for i in combi:
                b.append(list(i))
            return b
        
```

**Runtime: 76 ms, faster than 96.09% of Python3 online submissions for Combinations.
Memory Usage: 15.7 MB, less than 79.09% of Python3 online submissions for Combinations.**
