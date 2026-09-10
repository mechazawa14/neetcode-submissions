class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result  = []
        def backtracking(index , path):
            # base case aka goal or failure 
            if sum(path) == target :
                result.append(path[:])
                return
            if index == len(nums) or sum(path) > target:
                return 
            
            #we added one elem at this point in the path array 
            path.append(nums[index])
            #backtracking means we attempted to extend the branch from here to bottom
            #btw we had to keep index+1 as bro told each elem can be used only once 
            backtracking(index + 1 , path)
            #pop literally means that we backtrack to da point where we didnt have this last elem
            path.pop()
            #this time around we ought to make sure that same solution isnt coming again 
            while index+1 < len(nums)  and nums[index] == nums[index+1]:
                index += 1 
            backtracking(index+1, path)
            
        backtracking(0, [])
        return result 


            

                