class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows= len(grid)
        cols= len(grid[0])
        
        def dfs(r,c):
            neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
            if r<0 or c<0 \
            or r>=rows or c>=cols \
            or grid[r][c]==0:
                return 0
            
            grid[r][c]=0
            count =1

            for dr, dc in neighbors:
                count+= dfs(r+dr, c+dc)
            return count
        
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    max_area= max(dfs(r,c), max_area)

        return max_area
        