class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh,rotten=1,2
        rows,cols=len(grid),len(grid[0])
        num_fresh=0
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==fresh:
                    num_fresh+=1
                elif grid[r][c]==rotten:
                    q.append((r,c))
        num_min=-1  
        if num_fresh==0:
            return 0        
        while q:
            l= len(q)
            num_min+=1
            for _ in range(l):
                i,j=q.popleft()
                for r,c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0<=r<rows and 0<=c<cols and grid[r][c]==fresh:
                        num_fresh-=1
                        q.append((r,c))
                        grid[r][c]=rotten
        if num_fresh==0:
            return num_min
        return -1
            