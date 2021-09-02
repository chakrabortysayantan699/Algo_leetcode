# Soltuion 1

```python
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=['']
        
        for c in s:
            if c.isalpha():
                ans=[i+c.lower() for i in ans]+[i+c.upper() for i in ans]
            else:
                ans=[i+c for i in ans]
        return ans
```
**Runtime: 78 ms, faster than 20.71% of Python3 online submissions for Letter Case Permutation.
Memory Usage: 15.1 MB, less than 44.83% of Python3 online submissions for Letter Case Permutation.**