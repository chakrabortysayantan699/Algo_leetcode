# Solution 1

``` python
class Solution:
    def moveZeroes(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[j]=nums[i]
                j+=1
        for i in range(j,len(nums)):
            nums[i]=0
```

# Solution 2 (not accepted by leetcode because in-place exchanging not done but it works)

``` python
class Solution:
    def moveZeroes(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        b=[]
        d=[]
        for i in range (len(nums)):
            if(nums[i]==0):
                #nums.pop(i)
                b.append(0)
            else:
                d.append(nums[i])
        c=d+b
        nums=c
        return nums
```
