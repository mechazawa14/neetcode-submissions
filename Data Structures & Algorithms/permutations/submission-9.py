class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtracking(index,path):
            if index == len(nums):
                result.append(path[:])
                return
            for n in nums :
                if n in path :
                    continue
                else:
                    path.append(n)
                    backtracking(index + 1 , path)
                    path.pop()
        backtracking(0, [])
        return result