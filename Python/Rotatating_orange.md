# Solution 1

``` python
class Solution:
    def orangesRotting(self, grid) -> int:
        fresh = set()
        rotten = set()
        minute = 0
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 1:
                    fresh.add((r, c))
                elif v == 2:
                    rotten.add((r, c))
        while rotten and fresh:
            new_rot = set()
            for r, c in rotten:
                for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_tpl = (r + i, c + j)
                    if new_tpl in fresh:
                        fresh.remove(new_tpl)
                        new_rot.add(new_tpl)
            rotten = new_rot
            minute += 1
        return minute if not fresh else -1
 ```
 
