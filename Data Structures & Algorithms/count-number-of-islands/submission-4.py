class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        island_count = 0 
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r,c):
            if r>=0 and r<Rows and c>=0 and c<Cols and grid[r][c] == "1":
                grid[r][c]= "0"
                for dr,dc in directions:
                    dfs(r+dr, c+dc)
            return 

        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    island_count += 1
        return island_count 
