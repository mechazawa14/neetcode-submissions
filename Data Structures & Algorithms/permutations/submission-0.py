class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result  = []
        #literally the same as prev but this time we need permutations which mean 
        #combinations like [1,2,2] and [2,1,2] are considered different and allowed 

        def backtracking( path ):
            if len(path) == len(nums):
                result.append(path[:])
                return 
            for num in nums :
                if num in path :
                    continue 
                path.append(num)
                backtracking(path)
                path.pop()


        backtracking([])
        return result 
