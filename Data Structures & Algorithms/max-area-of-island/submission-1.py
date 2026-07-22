class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,cols= len(grid),len(grid[0])
        max_area=0
        visit=set()
        def bfs(r,c):
            q= deque()
            loc_area=0
            visit.add((r,c))
            q.append((r,c))
            while q:
                i,j=q.popleft()
                loc_area+=1
                for row,col in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=row<rows and 0<=col<cols and grid[row][col]==1 and (row,col) not in visit:
                        q.append((row,col))
                        visit.add((row,col))
            return loc_area
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visit:
                    max_area = max(max_area,bfs(i,j))
        
        return max_area