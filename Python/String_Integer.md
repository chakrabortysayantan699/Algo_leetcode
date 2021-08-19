# Solution 1
```python
class Solution:
    def myAtoi(self, s: str):
        a=['0','1','2','3','4','5','6','7','8','9']
        result=''
        flag= 0
        s=s.lstrip()
        if(0<len(s)<=200):
            if (s[0]=='+'):
                rel=1 
                s=s[1:]
                s=s.lstrip('0')   
            elif (s[0]=='-'):
                rel=-1
                s=s[1:]
                s=s.lstrip('0')
                #print('h',s)
            else:
                rel=0
                s=s.lstrip('0')
        else:
            result=''            
        for i in range(len(s)):
            #print(s[i])
            if (flag==0):
                if (s[i] in a):
                    result=result+s[i]
                    #print('here'+result)
                else:
                    flag=1
            else:
                break        
        
        if (result==''): 
            result=int("0")
        
        elif (rel==1 or rel==0):
            result='+'+result
            result=int (result)
        else:
            result='-'+result
            result=int (result)              
        
        if (-2**31<= int(result) <= (2**31)-1):
            return result
        elif(int(result)<-2**31):            
            result=str(-2**31)
            return(int(result))
        else:
            result=str((2**31)-1)
            return(int(result))           

   ```
