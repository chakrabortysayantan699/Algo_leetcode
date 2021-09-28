# Solution 1

```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans=set()
        for i in emails:
            local,domain=i.split('@')
            temp=''
            for k in local:
                if(k=='+' or k=='@'):
                    break
                elif(k=='.'):
                    local=local.replace('.','',1)
            for j in local:
                if(j=='+'):
                    break
                else:
                    temp+=j
            ans.add(temp+'@'+domain)
        return len(ans)
  ```
  
