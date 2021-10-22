# Solution 1

``` python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=''
        res=[]
        for i in digits:
            ans+=str(i)
        ans1=int(ans)+1
        for i in str(ans1):
            res.append(int(i))
        return res
        
 ```
 
