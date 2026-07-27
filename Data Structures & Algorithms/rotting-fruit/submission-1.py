from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        # find all rotten fruits at start
        # add them to queue that is minute zero
        # then explore its all neibours add levels(minutes by 1)
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visit= set()
        fresh_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j,0)) # adding the levels
                    visit.add((i,j))
                elif grid[i][j]==1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        minutes = 0
        while queue:
            r, c, minutes = queue.popleft()

            neighbours= [(1,0),(-1,0),(0,1),(0,-1)]
            for dr, dc in neighbours:
                nr = r+dr
                nc= c+dc

                if nr<0 or nc<0 or nr>=rows or nc>=cols \
                    or (nr,nc) in visit \
                    or grid[nr][nc]==0:
                    continue
                queue.append((nr,nc,minutes+1))
                visit.add((nr,nc))
                fresh_count -= 1
        
        return minutes if fresh_count == 0 else -1