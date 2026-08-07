class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visit = set()

        def dfs(i,j):
            if (i not in range(rows) or j not in range(cols) or
            grid[i][j]==0):
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            perimeter = dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
            return perimeter
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return dfs(i,j)

        return 0