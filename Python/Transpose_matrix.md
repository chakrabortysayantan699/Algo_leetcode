# Solution 1

``` python

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        temp=[]
        result=[]
        for i in range(len(matrix[0])):
            for j in matrix:
                temp.append(j[i])
            result.append(temp)
            temp=[]
        return result
  ```
  
        
