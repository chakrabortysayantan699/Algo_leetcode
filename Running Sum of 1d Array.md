# Solution 1

```python

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=0
        ans=[]
        for i in range(len(nums)):
            if(i==0):
                ans.append(nums[i])
            elif(i>0):
                for j in range(i+1):
                    a+=nums[j]
                ans.append(a)
                a=0
        return ans
  ```
  
            
                
