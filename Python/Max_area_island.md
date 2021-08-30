# Soltuion 1

``` python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
		# i for column, j for row
        # DFS through every adjacent node from start
        def calculate_area(i, j):
            area = 1
            grid[j][i] = 0
            if i + 1 < len(grid[0]) and grid[j][i + 1] == 1:
                area += calculate_area(i + 1, j)
            if i - 1 >= 0 and grid[j][i - 1] == 1:
                area += calculate_area(i - 1, j)
            if j + 1 < len(grid) and grid[j + 1][i] == 1:
                area += calculate_area(i, j + 1)
            if j - 1 >= 0 and grid[j - 1][i] == 1:
                area += calculate_area(i, j - 1)
            return area
        
        # For debugging
        def print_grid(j, i, grid):
            print("[j, i] = [{}, {}], node = {}".format(j, i, grid[j][i]))
            for row in grid:
                print(row)
            print()
        
        # Go through every node in the grid
        max_area = 0
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == 1:
                    max_area = max(calculate_area(i, j), max_area)
                    # print_grid(j, i, grid)
                
        return max_area
```
