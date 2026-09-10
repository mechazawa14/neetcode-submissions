class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        #to avoid similar combos like [1,2,2] and [2,1,2] for a target 5 lets sort it first 
        #so that during the left/1st time itself we get the combos where same nos come 
        # consecutively 
        candidates.sort()
        def backtracking(index, path, totalsum):
            # 1. goal/failure
            if totalsum == target:
                result.append(path[:])
                return

            if totalsum > target or index == len(candidates):
                return 
            
            # 2. left choice 
            path.append(candidates[index])
            backtracking(index+1 , path , totalsum + candidates[index])
            #3.cleanse
            path.pop()
            #4.right choice 
            while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                index+=1 
            backtracking(index+1 , path, totalsum)

        backtracking(0 , [], 0)
        return result 