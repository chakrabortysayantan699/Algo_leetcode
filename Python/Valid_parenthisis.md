# solution 1

``` python

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if(i==')' or i=="}"or i==']'):
                if(len(stack)>=1):
                    if(i==')'):
                        if(stack[-1]=='('):
                            stack.pop()
                        else:
                            return False
                    elif(i=='}'):
                        if(stack[-1]=='{'):
                            stack.pop()
                        else:
                            return False
                    elif(i==']'):
                        if(stack[-1]=='['):
                            stack.pop()
                        else:
                            return False
                else:
                    return False
            else:
                stack.append(i)
        if(len(stack)==0):
            return True
        else:
            return False
```
