class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        right = len(matrix) -1 
        while left <=  right :
            mid = (left + right) // 2 
            left_inarray = 0  
            right_inarray = len(matrix[mid])-1  
            while left_inarray <= right_inarray :
                mid_inarray = (left_inarray+right_inarray)//2
                if matrix[mid][mid_inarray] == target :
                    return True 
                if  matrix[mid][mid_inarray]< target:
                    left_inarray = mid_inarray+ 1 
                if matrix[mid][mid_inarray] > target:
                    right_inarray = mid_inarray- 1
            
            if target< matrix[mid][0] :
                right = mid -1 
            if target > matrix[mid][0]:
                left  = mid + 1 
        
        return False 


