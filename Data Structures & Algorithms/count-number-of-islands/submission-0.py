class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        islands = 0
        rows,cols = len(grid),len(grid[0])

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c]=="0" or (r,c) in visit:
                return
            visit.add((r,c))
            row = [1,0,0,-1]
            col = [0,1,-1,0]
            for k in range(4):
                dfs(r+row[k],c+col[k])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    dfs(r,c)
                    islands+=1
        return islands            