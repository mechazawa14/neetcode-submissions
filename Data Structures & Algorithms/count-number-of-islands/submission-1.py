class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0
        visited = set()
        islands = 0
        rows , cols = len(grid), len(grid[0])

        def bfs(r, c):
            visited.add((r,c))
            directions  = [(-1,0),(1,0),(0,1),(0,-1)]
            queue = deque([(r,c)])
            while queue: 
                row,col = queue.popleft()
                for dr , dc in directions :
                    row1, col1 = dr+row , dc+col
                    if (row1 in range(rows)) and (col1 in range(cols)) and grid[row1][col1]=="1" and ((row1, col1) not in visited):
                       visited.add((row1, col1))
                       queue.append((row1, col1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands  += 1
                    bfs(r,c)
        return islands

