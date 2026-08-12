class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        visit=set()
        q = deque()

        def addcell(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c]==-1:
                return
            else:
                q.append([r,c])
                visit.add((r,c))
                return   
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append([r,c])
                    visit.add((r,c))
        dist = 0 
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c-1)
                addcell(r,c+1)
                grid[r][c] = dist
            dist+=1

                           
