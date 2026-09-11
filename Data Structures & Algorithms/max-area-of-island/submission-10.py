class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        maxarea = 0  
        rows , cols = len(grid), len(grid[0]) 
        visited = set()

        # bfs being created for the  sole purpose of visiting all the adjacent 1s
        def bfs(row , col):
            area = 1
            q = collections.deque()
            q.append((row, col))
            visited.add((row, col))
            directions = [[1, 0], [0,1], [-1, 0], [0, -1]]
            while q:
                row , col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range (cols) and 
                        grid[r][c] == 1 and 
                        (r, c) not in visited):
                        visited.add((r, c))
                        q.append((r,c))
                        area  = area +1 
            return area 

        # simply traversing 
        for row in range(rows):
            for col in range (cols):
                if grid[row][col] == 1 and (row , col) not in visited:
                    visited.add((row, col))
                    area1 = bfs(row, col)
                    maxarea = max(maxarea, area1)
                    
                     
        return maxarea 
                    