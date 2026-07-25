from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # use bfs (it explores all neighbours at once)
        rows = len(image)
        cols = len(image[0])

        queue = deque()
        visit = set()
        queue.append((sr,sc))
        src_color = image[sr][sc]
        image[sr][sc]= color
        visit.add((sr,sc))

        while queue:
            r,c = queue.popleft()

            #neighbours
            neighbours = [(-1,0),(1,0),(0,1),(0,-1)]
            for dr,dc in neighbours:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or \
                    nr>=rows or nc>=cols \
                    or (nr,nc) in visit:
                    continue
                
                if image[nr][nc] == src_color:
                    image[nr][nc]=color
                    queue.append((nr,nc))
                    visit.add((nr, nc))
        return image
