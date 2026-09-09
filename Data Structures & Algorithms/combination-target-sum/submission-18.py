class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = [] 

        def backtracking(index , path, totalsum):
            if index == len(nums):
                return 
            if totalsum> target:
                return 
            if totalsum == target:
                result.append(path[:])
                return 
            
            path.append(nums[index])
            backtracking(index, path, totalsum = totalsum + nums[index])
            path.pop()
            backtracking(index+1, path, totalsum)
        backtracking(0, [],  0)
        return result
            





                