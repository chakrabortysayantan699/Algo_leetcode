# Solution 1
class Solution(object):
```python
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        cnt1, cnt2 = [0] * 26, [0] * 26
        diff = 0
        for s in s1:
            if not cnt1[ord(s) - ord('a')]:
                diff += 1
            cnt1[ord(s) - ord('a')] += 1
        for s in s2[:len(s1)]:
            cnt2[ord(s) - ord('a')] += 1
            if cnt1[ord(s) - ord('a')] == cnt2[ord(s) - ord('a')]:
                diff -= 1
        if diff == 0:
            return True
        p1 = 0
        for p2 in range(len(s1), len(s2)):
            cnt2[ord(s2[p2]) - ord('a')] += 1
            if cnt1[ord(s2[p2]) - ord('a')] == cnt2[ord(s2[p2]) - ord('a')]:
                diff -= 1
            if cnt1[ord(s2[p1]) - ord('a')] == cnt2[ord(s2[p1]) - ord('a')]:
                diff += 1
            cnt2[ord(s2[p1]) - ord('a')] -= 1
            if diff == 0:
                return True
            p1 += 1
            p2 += 1
        return False
 ```
# Solution 2 by inbuild function

```python
from itertools import permutations as per
class Solution:
    def checkInclusion(self, s1, s2):
        flag=False
        if((1<=len(s1)<=10**4) and (1<=len(s2)<=10**4)):
            a=per(s1)
            b=list(a)
            for i in b:
                c="".join(i)
                if c in s2:
                    flag=True
                    return flag
        return flag
```
