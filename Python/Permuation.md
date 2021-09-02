# Solution 1 (With inbuild function)

``` python
from itertools import permutations as per
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a=[]
        if (1<=len(nums)<=6):
            perm=per(nums)
            for i in perm:
                a.append(list(i))
            return a
        
```
**Runtime: 51ms, faster than 90.71% of Python3 online submissions for Letter Case Permutation.
Memory Usage: 14.1 MB, less than 84.83% of Python3 online submissions for Letter Case Permutation.**