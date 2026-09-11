class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result  =  []
        board  = [['.']*n for i in range (n)]
        colset  = set()
        posdiags = set()
        negdiags = set()

        def backtracking(r):
            # if current row = total no of queeens , its done bro 
            if r ==  n:
                rowinstringelems  = ["".join(row) for row in board]
                result.append(rowinstringelems)
                return 
            for c in range(n):
                if ( c in colset ) or (r+c in posdiags ) or (r-c in negdiags):
                    continue 
                colset.add(c)
                posdiags.add(r+c)
                negdiags.add(r-c)
                board[r][c] = 'Q'
                backtracking(r+1)
                colset.remove(c)
                posdiags.remove(r+c)
                negdiags.remove(r-c)
                board[r][c] = "."
        backtracking(0)
        return result
