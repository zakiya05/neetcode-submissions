class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visit= set()
        ni=0
        rows, cols =len(grid), len(grid[0])

        def bfs(row,col):
            q = collections.deque()
            visit.add((row,col))
            q.append((row,col))
            while q:
                i , j = q.popleft()
                for r, c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0<= r< rows and 0<= c < cols and grid[r][c] == "1" and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))
                        
                        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    ni+=1

        return ni



        
        