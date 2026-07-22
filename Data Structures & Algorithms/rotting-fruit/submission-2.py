class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        FRESH, ROTTEN =1,2
        rows , cols = len(grid), len(grid[0])

        num_fresh = 0
        min_t =-1
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == FRESH:
                    num_fresh +=1
                elif grid[r][c] ==ROTTEN:
                    q.append((r,c))
        if num_fresh ==0:
            return 0
        while q:
            l = len(q)
            min_t+=1
            for k in range(l):
                i,j = q.popleft()
                for r, c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0<= r < rows and 0 <= c < cols and grid[r][c] == FRESH:
                        num_fresh-=1
                        q.append((r,c))
                        grid[r][c]=ROTTEN
        if num_fresh ==0:
            return min_t
        else:
            return -1
