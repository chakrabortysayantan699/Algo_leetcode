# Solution 1

``` python
class Solution:
    def reverseWords(self, s: str) -> str:
        d=''
        a=""
        def reverse(s):
            str = ""
            for i in s:
                str = i + str
            return str
        if(len(s)>1):
            for i in s:
                if (i!=' '):
                    a+=i
                elif (i==' ') :
                    b= reverse (a)
                    a=''
                    d+=b
                    d+=" "
            
            b=reverse(a)
            d+=b
            return d
        elif(len(s)==1):
            return s

```
