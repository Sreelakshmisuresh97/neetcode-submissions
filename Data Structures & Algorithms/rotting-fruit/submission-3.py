class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh,time = 0,0
        q = deque()
        ROWS,COLS=len(grid),len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit=set()
        while q and fresh>0:
            length = len(q)
            for i in range(length):
                row,col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c]==1):
                        grid[r][c]=2
                        q.append((r,c))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
                            
        