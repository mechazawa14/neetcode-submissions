class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        #base case
        def backtracking(index , path):
            if index == len(nums):
                result.append(path[:])
                return 
            #left choice 
            path.append(nums[index])
            backtracking(index+1 , path)

            path.pop()

            #right choice 
            backtracking(index+1 , path)
        backtracking(0, [])
        return result 
