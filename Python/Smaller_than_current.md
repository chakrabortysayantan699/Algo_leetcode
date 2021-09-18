# Solution 1

``` python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        res=nums.sort(reverse=True)
        ans=[]
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]>nums[j]):
                    count+=1
            ans.append(count)
            count=0       
        
        '''
        ans=[]
        count=0
        for i in nums:
            for j in range(len(nums)):
                if(i>nums[j]):
                    count+=1
            ans.append(count)
            count=0
        return ans
```
                
            
            
        
