class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS,COLS = len(grid), len(grid[0])
        islands=0
        
        def dfs(i,j):
            if (i<0 or j<0 or i>=ROWS or j>=COLS or grid[i][j]=="0"):
                return 
            grid[i][j] ="0"
            for r,c in directions:
                dfs(r+i,c+j)
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=="1":
                    dfs(i,j)
                    islands+=1
        return islands
