class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def backtracking(r, c, word_index):
            # 1. Goal: Found all characters of the word
            if word_index == len(word):
                return True
                
            # 2. Failure Constraints: Out of bounds OR wrong character
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                board[r][c] != word[word_index]):
                return False
            
            # Save original character to restore it during the cleanse step
            temp = board[r][c]
            
            # Mark as visited so this specific path doesn't loop back to it
            board[r][c] = "#"
            
            # 3. Explore Branches: Try all 4 adjacent directions
            # We use "or" because if ANY path returns True, we win!
            found = (backtracking(r + 1, c, word_index + 1) or  # Down
                     backtracking(r - 1, c, word_index + 1) or  # Up
                     backtracking(r, c + 1, word_index + 1) or  # Right
                     backtracking(r, c - 1, word_index + 1))    # Left
            
            # 4. Cleanse: Restore the cell for other starting paths
            board[r][c] = temp
            
            return found

        # Because the word can start anywhere, we try every cell as a starting point
        for r in range(ROWS):
            for c in range(COLS):
                if backtracking(r, c, 0):
                    return True
                    
        return False
