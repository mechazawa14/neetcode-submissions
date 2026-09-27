class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,  r = 0 ,  len(matrix[0]) -1 
        
        while l< r:
            for i in range(r-l):
                top , bottom  = l, r 
                # storing the top left in a temporary variable 
                topleft = matrix[top][l+i]
                # storing the bottom left in the top lefts place 
                matrix[top][l+i]  = matrix[bottom-i][l]
                # storing the bottom right in the bottom lefts place 
                matrix[bottom-i][l] = matrix[bottom][r-i]
                # storing the top right in the bottom rights place 
                matrix[bottom][r-i] = matrix[top+i][r]
                # storing the top left whch we stored initially in top right 
                matrix[top+i][r] = topleft
            l+=1
            r-=1
                
