# Solution 1

``` python
class Solution:
    def rotate(self, nums: List[int], k: int) :
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)-1
        for i in range(k):
            c=nums[n]
            nums.pop(n)
            nums.insert(0,c)
        return nums
        
``` 
