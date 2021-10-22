# Solution 1

``` python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        return self.bs(nums, 0, len(nums)-1, len(nums)-1)
    
    def bs(self, arr, start, end, arrLen):
        if start > end:
            return -1
        else:
            mid = (start + end) // 2
            if mid == 0:
                if arr[mid] > arr[mid+1]:
                    return mid
                else:
                    return self.bs(arr, mid+1, end, arrLen)
            elif mid == arrLen:
                if arr[mid] > arr[mid-1]:
                    return mid
                else:
                    return self.bs(arr,start,mid-1,arrLen)
            elif arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            else:
                if arr[mid+1] > arr[mid]:
                    return self.bs(arr, mid+1, end, arrLen)
                elif arr[mid-1] > arr[mid]:
                    return self.bs(arr, start, mid-1, arrLen)
 ```
 
