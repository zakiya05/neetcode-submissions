class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visit =set()

        def dfs(i,j):
            print("in dfs")
            if i<0 or j<0 or i==ROWS or j==COLS or grid[i][j]==0 or (i,j) in visit:
                return 0
            visit.add((i,j))
            return (1+ dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)) 
            
            
        maxlen= 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maxlen = max(maxlen, dfs(i,j))
        return maxlen