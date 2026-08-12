class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        rows,cols = len(grid),len(grid[0])
        maxarea = 0

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c]==0 or (r,c) in visit:
                return 0   
            visit.add((r,c))
            area = 1
            row = [1,0,0,-1]
            col = [0,1,-1,0]
            for k in range(4):
                area = area+dfs(r+row[k],c+col[k])
            return area  

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    maxarea = max(maxarea,dfs(r,c))
                   #islands+=1
        return maxarea            