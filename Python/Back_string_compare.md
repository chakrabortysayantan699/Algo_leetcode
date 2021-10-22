# Solution 1

```python

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backSpace(s:str):
            s1=''
            result=[]
            for i in range(len(s)):
                if(s[i]!='#'):
                    result.append(s[i])
                elif(s[i]=='#'):
                    n=len(result)
                    if(n>=1):
                        # result.remove(result[n-1])
                        del result[n-1]
                    else:
                        continue
            for i in result:
                s1+=i
            return s1
        ans1=backSpace(s)
        ans2=backSpace(t)
        if(ans1==ans2):
            return True
        else:
            return False
                        
 ```
 
    
