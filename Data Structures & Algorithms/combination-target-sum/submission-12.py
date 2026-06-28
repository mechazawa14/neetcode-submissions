class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtracking(index, path , sum):
            if sum == target :
                result.append(path[:])
                return 
            if index == len(nums) or sum > target :
                return 
            path.append(nums[index])
            backtracking(index, path, sum+nums[index])
            path.pop()
            backtracking(index +1, path, sum)
        backtracking(0 , [], 0)
        return result 