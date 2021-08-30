# Solution 1

``` python 
# Greedy
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        p = 0
        #dictionary for avoiding duplicates 
        d = {}
        for i, c in enumerate(s):
            if c not in d or d[c] < p:
                ans = max(ans, i - p + 1)
            else:
                p = d[c] + 1
            d[c] = i
        return ans
```

