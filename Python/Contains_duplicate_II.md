# Solution 1

``` python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        flag= False
        def check(nums,k):           
            for i in range(len(nums)-k):
                if(nums[i]==nums[i+k]):                    
                    return True                  
                    
        if(1<=len(nums)<=10**5):
            for i in range(k+1):
                if(i>0):
                    flag=check(nums,i)
                    if(flag==True):
                        return flag
            return flag
        else:
            return flag 
        
```

                
        
        
