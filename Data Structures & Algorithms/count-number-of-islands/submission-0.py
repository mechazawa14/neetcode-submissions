from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            visited.add((r, c))
            queue = deque([(r, c)])  # Initialize queue with the tuple (r, c)
            while queue:
                row, col = queue.popleft()  # Dequeue the front element
                directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    row1, col1 = row + dr, col + dc
                    if (row1 >= 0 and row1 < rows) and (col1 >= 0 and col1 < cols) and ((row1, col1) not in visited) and (grid[row1][col1] == "1"):
                        visited.add((row1, col1))
                        queue.append((row1, col1))  # Add the neighbor to the queue

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        
        return islands
