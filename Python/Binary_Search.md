# Solution 1

``` python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low=0
        high=len(nums)-1
        
        def binary(nums,low,high,target):
            
            if(low<=high):
                mid=(low+high)//2
                if (nums[mid]==target):
                    return mid
                elif(nums[mid]>target):                
                    return binary(nums,0,mid-1,target)
                else:
                    return binary(nums,mid+1,high,target)
            else:
                return -1
        
        a=binary(nums,low,high,target)
        return a
```
