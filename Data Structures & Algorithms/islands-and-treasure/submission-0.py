class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit=set()
        q = deque()
        INF= 2147483647

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visit.add((i,j))
                    q.append([i,j])
        dist=0
        while q:
            dist+=1
            l = len(q)
            for i in range(l):
                i,j = q.popleft()
                for r,c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0 <= r< rows and 0<= c < cols and grid[r][c] == INF and (r,c) not in visit:
                        grid[r][c] = dist
                        q.append([r,c])
                        visit.add((r,c))
            
        return 