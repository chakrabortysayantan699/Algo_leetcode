# Solution 1

``` python

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        great=max(candies)
        for i in candies:
            a=i+extraCandies
            if (great<=a):
                ans.append(True)
            else:
                ans.append(False)
        return ans
        
  ```
  
