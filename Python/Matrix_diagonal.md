# Solution 1

``` python

class Solution:
    def diagonalSum(self, mat: List[List[int]]):
        i=0
        result=[]
        for j in mat:
            result.append(j[i])
            j[i]=0
            i+=1
        i-=1
        for j in mat:
            result.append(j[i])
            j[i]=0
            i-=1
        res=sum(result)  
        return res   
   
```

            
       
        
        
