# solution 1

``` python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n=len(nums)
        even=[]
        odd=[]
        ev=0
        od=0
        for i in nums:
            if (i%2==0):
                even.append(i)
            else:
                odd.append(i)
        nums=[]
        for i in range(n):
            if (i%2==0):
                nums.append(even[ev])
                ev+=1
            else:
                nums.append(odd[od])
                od+=1
        return nums
  ```
  
