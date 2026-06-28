class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result  = []
        candidates.sort()
        def backtracking(index, path, sum):
            if sum == target :
                result.append(path[:])
                return 
            if sum > target or index == len(candidates):
                return 
            path.append(candidates[index])
            backtracking(index+1, path , sum+candidates[index])
            path.pop()
            while index+1 < len(candidates) and (candidates[index]==candidates[index+1])   :
                index+=1 
            backtracking(index+1, path , sum)
        backtracking(0, [], 0)
        return result 