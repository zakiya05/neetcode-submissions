class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        max_islands =0
        visit=set()

        def bfs(i,j):
            q = deque()
            visit.add((i,j))
            q.append((i,j))
            while q:
                i, j = q.popleft()
                for r,c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0<= r< rows and 0<= c <cols and grid[r][c]=="1" and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visit:
                    bfs(i,j)
                    max_islands+=1

        return max_islands
