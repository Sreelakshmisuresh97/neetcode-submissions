class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visit = set()
        q = deque()
        fresh=0
        def addcell(r,c,fresh):
            if r  in range(rows) and c  in range(cols)  and grid[r][c]==1:
                fresh-=1
                grid[r][c]=2
                q.append((r,c))
            
                return   
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                   
                    q.append((r,c))
        time = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh>0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
