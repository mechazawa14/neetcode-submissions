class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0 
        rows , cols = len(grid), len(grid[0])
        # making a set visited that stores places which weve visited as in (row, col)
        visited = set()
        islandcount  = 0

        def bfs(row, col):
            que  = deque([(row, col)])
            visited.add((row , col))
            directions  = [[1,0], [-1, 0], [0,1], [0, -1]]

            while que:
                r, c = que.popleft()
                directions = [[1,0], [0,1], [-1, 0], [0, -1]]
                for dr, dc in directions :
                    ro, co = r + dr, c+ dc
                    if (ro in range(rows) and 
                        co in range(cols) and 
                        grid[ro][co] == "1" and 
                        (ro, co) not in visited):
                        visited.add((ro,co))
                        que.append((ro, co))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited :
                    bfs(r,c)
                    islandcount+=1
        return islandcount





        
