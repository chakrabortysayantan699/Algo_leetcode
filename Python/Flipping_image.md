# Solution 1

``` python 

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in image:
            b=i[::-1]
            result.append(b)
        for i in result:
            for j in range(len(i)):
                if(i[j]==0):
                    i[j]=1
                elif(i[j]==1):
                    i[j]=0
        return result
```
