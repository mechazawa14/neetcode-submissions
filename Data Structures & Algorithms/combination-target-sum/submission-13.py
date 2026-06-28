class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtracking(index, path, total_sum):

            #1. goal 
            if total_sum == target :
                result.append(path[:])
                return 
            if index == len(nums) or total_sum > target : #or failure 
                return 

            path.append(nums[index])
            #2. left choice as long as we want(no increment in index) ,
            #  tbh until the base condition breaks 
            backtracking(index, path , total_sum + nums[index])
            path.pop() #3. cleanse 

            # 4.right choice 
            #  Move to index + 1 so we never look at this number again
            backtracking(index+1, path , total_sum)
        backtracking(0 , [], 0)
        return result 





            