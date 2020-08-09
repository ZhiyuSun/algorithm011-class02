from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def _dfs(i, j):
            if i < 0 or j < 0 or i >= m or j>= n or grid[i][j] == '0': 
                return 
            grid[i][j] = '0'
            _dfs(i, j+1)
            _dfs(i, j-1)
            _dfs(i+1, j)
            _dfs(i-1 , j)

        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        count = 0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    count += 1
                    _dfs(i, j)
        return count