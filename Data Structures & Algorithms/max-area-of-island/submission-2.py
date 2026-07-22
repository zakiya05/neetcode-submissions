class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        max_area=0
        visit=set()
        q = deque()
        def bfs(row,col):
            visit.add((row,col))
            q.append((row,col))
            loc_area=0
            while q:
                loc_area+=1
                i,j = q.popleft()
                for r,c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0<=r<rows and 0<=c<cols and grid[r][c]==1 and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
            return loc_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    max_area=max(max_area,bfs(r,c))
        return max_area