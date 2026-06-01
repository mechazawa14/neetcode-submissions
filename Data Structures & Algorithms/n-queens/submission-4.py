class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result  = []
        cols  = set()
        posdiags = set()
        negdiags  = set()
        board  = [["."]*n for _ in range(n)]
        def backtracking(r):
            if r==n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return 
            for c in range(n):
                if c in cols or (r+c) in posdiags or (r-c) in negdiags:
                    continue 
                cols.add(c)
                posdiags.add(r+c)
                negdiags.add(r-c)
                board[r][c] = "Q"

                backtracking(r+1)

                cols.remove(c)
                posdiags.remove(r+c)
                negdiags.remove(r-c)
                board[r][c]= "."
        backtracking(0)
        return result
                