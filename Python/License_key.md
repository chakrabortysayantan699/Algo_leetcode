# Solution 1

```python

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        j=1
        s=s.replace('-','')
        new_s=s[::-1]
        result=''
        for i in range(len(new_s)):
            if(i==((k*j)-1)):
                result+=new_s[i]
                if(i!=len(new_s)-1):
                    result+='-'
                    j+=1
            else:
                result+=new_s[i]
        final=result[::-1]
        final_result=final.upper()
        return final_result

 ```
 
