class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row]  or 
                    board[row][col] in cols[col]  or 
                    board[row][col] in box[(row//3, col//3)]) :
                    return False 
                else:
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col]) 
                    box[(row//3, col//3)].add(board[row][col])
        return True 



