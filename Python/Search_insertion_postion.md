# Solution 1

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high=len(nums)-1
        low=0
        def binarySearch(nums,low,high,target):
            if(low<=high):
                mid=(low+high)//2
                if(nums[mid]==target):
                    return mid
                            
                elif(nums[mid]<target):
                    if(  mid>len(nums)-1 and nums[mid+1]>target>nums[mid]):
                        #nums.insert(mid+1,target)
                        return (mid+1)
                    elif(mid==len(nums)-1):
                        if(nums[mid]<target):
                            #nums.insert(mid+1,target)
                            return mid+1  
                    return binarySearch(nums,mid+1,high,target)
                else:
                    if(mid>0  and nums[mid]>target>nums[mid-1] ):
                        return (mid)
                    elif(mid==0):
                        if(nums[mid]>target):
                            return 0
                    return binarySearch(nums,low,mid-1,target)
        a=binarySearch(nums,low,high,target)
        return a
```
    
         
        
            
            
            
        
