# Solution 1

``` python
class Solution:
    def reverse(self, x: int) :
                    
        z=''
        y=str(x)
        
        if(x<0):
            a=y[1:]
        else:
            a=y
        
        if(len(a)==1):
            return x        
        
        z+=a[::-1]
                
        if(z=='0'):
            return z
        
        if(x<0):
            ans='-'+z.lstrip('0')
            ab=int(ans)
        else:
            ans= z.lstrip('0')
            ab=int(ans)
        
        if -2 ** 31 <= ab <= 2 ** 31 - 1:
            return ab 
        return 0
            
```
