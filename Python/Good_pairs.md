# Solution 1

```python

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=0
        d=[]
        '''
        def result(ct):
            ans=(ct *(ct-1))//2
            return ans
        
        '''        
        
        for i in nums:
            if(i not in d):
                d.append(i)
                ct=nums.count(i)
                ans+=((ct *(ct-1))//2)
        return ans
```

                
    
