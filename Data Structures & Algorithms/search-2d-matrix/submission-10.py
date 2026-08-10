class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0 
        high  = len(matrix) -1 
        while low <= high :
            mid = low + (high - low)//2 
            low_inarray  = 0 
            high_inarray  = len(matrix[mid])-1
            while low_inarray <= high_inarray : 
                mid_inarray = low_inarray + (high_inarray - low_inarray)//2
                if matrix[mid][mid_inarray] == target :
                    return True 
                elif matrix[mid][mid_inarray] < target :
                    low_inarray = mid_inarray+1 
                if matrix[mid][mid_inarray] > target :
                    high_inarray = mid_inarray-1 
            if matrix[mid][0] > target :
                high  = mid -1 
            elif matrix[mid][len(matrix[mid])-1] < target :
                low = mid + 1 
            else:
                return False 
        return False 

                