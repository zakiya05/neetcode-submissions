class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid), len(grid[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        q = deque()
        fresh_fruit = 0
      
        time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                   
                if grid[i][j] == 1:
                    fresh_fruit+=1
       
        
        while fresh_fruit > 0 and q:
            l = len(q)
            time +=1
            for i in range(l):
                r,c = q.popleft()
                
                for dr, dc in directions:
                    row, col = dr+r, dc+c 
                    if (row in range(rows)) and col in range(cols) and grid[row][col]==1:
                        q.append((row,col))
                        grid[row][col] = 2
                        fresh_fruit -=1
                   
        return time if fresh_fruit == 0 else -1


                