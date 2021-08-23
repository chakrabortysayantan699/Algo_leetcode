# Solution 1

``` python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i1, i2 = 0, len(numbers)-1
        while numbers[i1] + numbers[i2] != target:
            if numbers[i1] + numbers[i2] > target:
                i2 -= 1
            else:
                i1 += 1
        
        return [i1+1, i2+1]
```
# Solutuion II (not optimal)

``` python
class Solution(object):
    def twoSum(self, numbers, target):
    c=len(numbers)
        if((2<= c <=3*(10**4)) and (-1000<=target<=1000) ):
            for i in range(len(numbers)):
                for j in range(len(numbers)):
                    if(i!=j):
                        if((numbers[i]+numbers[j])==target):
                            c=[i+1,j+1]
                            return c
```

