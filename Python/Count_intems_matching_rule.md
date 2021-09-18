# Solution 1

``` python 

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        if(ruleKey=="type"):
            j=0
        elif(ruleKey=="color"):
            j=1
        elif(ruleKey=="name"):
            j=2
        '''
        for i in range(len(items)):        
        '''
        for i in items:
            if(i[j]==ruleValue):
                count+=1
        return count
 ```
 
                
            
            
        
