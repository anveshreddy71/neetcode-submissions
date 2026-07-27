from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if not grid or grid[0][0]==1 or grid[-1][-1]==1:
            return -1

        #shortest path is matrix bfs problem
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        visit = set()

        # append top left corner to queue
        queue.append((0,0,1))
        visit.add((0,0))

        while queue:
            # pop first element in queue
            r,c, length = queue.popleft()
            # return length if r and c are bottom right
            if r==rows-1 and c== cols-1:
                return length

            #declare neighbours
            neighbours = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),
            (-1,1),(1,1),(1,-1)]

            for nr, nc in neighbours:
                dr = r + nr
                dc = c+ nc
                if dr<0 or dc<0 or dr>=rows or dc>=cols \
                    or (dr,dc) in visit \
                    or grid[dr][dc]==1:
                    continue
                
                queue.append((dr,dc, length + 1))
                visit.add((dr,dc))
        
        return -1