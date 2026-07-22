class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        max_area = 0

        def bfs(r,c):
            l_a = 0
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                l_a+=1
                i,j = q.popleft()
                for x, y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0<= x < rows and 0<= y < cols and grid[x][y] == 1 and (x,y) not in visit:
                        q.append((x,y))
                        visit.add((x,y))
            return l_a           
                


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visit:
                    max_area = max(bfs(i,j), max_area)
        return max_area
