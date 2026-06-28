class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result  = []
        def backtracking(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for n in nums :
                if n in path:
                    continue 
                path.append(n)
                backtracking(path)
                path.pop()
            # backtracking(path)
        backtracking([])
        return result