# Solution 1

``` python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        if(1<=n<=10**5):
            if(n>1):
                for i in range(n//2):
                    s[n-i-1] ,s[i]=s[i], s[n-i-1]
 ```
