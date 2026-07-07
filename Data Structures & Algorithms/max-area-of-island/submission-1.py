class Solution:
    def  maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0

        visited = set()
        islands = 0
        rows , cols = len(grid), len(grid[0])
        maxarea = 0
        areas  = []
        def bfs(r,c):
            nonlocal maxarea 
            queue = deque([(r,c)])
            directions  = [[-1,0],[1,0],[0,-1],[0,1]]
            visited.add((r,c))
            area = 1
            while queue:
                row, col = queue.popleft()
                for dr,dc in directions :
                    row1, col1 = row+dr , col+dc
                    if (row1  in range(rows)) and (col1 in range(cols)) and (grid[row1][col1]==1) and (row1, col1) not in visited:
                       visited.add((row1, col1))
                       queue.append((row1, col1))
                       area+=1
                maxarea = max(maxarea, area)
            return maxarea

                    
                    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited :
                    
                    currentarea = bfs(r,c)
                    maxarea = max(maxarea, currentarea)
                     
        return maxarea
