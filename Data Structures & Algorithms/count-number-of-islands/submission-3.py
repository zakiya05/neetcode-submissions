class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 
        Rows, Cols = len(grid), len(grid[0])
        directions = [[-1,0],[0,-1],[0,1],[1,0]]

        def dfs(r,c):
            if r<0 or r>=Rows or c <0 or c>= Cols or grid[r][c]=="0":
                return 
            grid[r][c] = "0"
            for dr, dc in directions: 
                dfs(dr+r, dc+c)

        islands = 0 
        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands+=1
        print(grid)
        return islands

