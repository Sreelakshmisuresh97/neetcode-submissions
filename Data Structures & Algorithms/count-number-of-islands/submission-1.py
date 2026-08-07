class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visit = set()
        rows,cols = len(grid),len(grid[0])
        def dfs(i,j):
            if(i not in range(rows) or j not in range(cols) or grid[i][j]=="0" or (i,j) in visit):
                return
            visit.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visit:
                    dfs(i,j)
                    res+=1
        return res


