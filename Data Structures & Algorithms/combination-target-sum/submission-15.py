class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        #inititally made an empty array for storing the ans subsets 

        #making the base cases 
        def backtracking (index, path):
            if index == len(nums):
                return 
            if (sum(path)>target):
                return 
            if sum(path) == target :
                result.append(path[:])
                return 
            
            #signifying the left choices
            path.append(nums[index])
            #not adding +1 to the index as same number can be used any number of times 
            backtracking(index , path)
            #change to next branch
            path.pop()
            #right choice
            backtracking(index+1 , path)
        backtracking(0 , [])
        return result 
