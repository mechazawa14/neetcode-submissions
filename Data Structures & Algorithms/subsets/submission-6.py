class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result  = []

        def backtracking(index, path):
            #1. goal 
            if index == len(nums) : #if index == 3 > 2(max index)
                result.append(path[:])
                return 
            #2.left choice 
            path.append(nums[index])
            backtracking(index+1, path)
            path.pop() #3.clean up 

            #4. right choice 
            backtracking(index+1, path)
        backtracking (0 , [])
        return result
