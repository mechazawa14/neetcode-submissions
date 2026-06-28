class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 1. Sort first so duplicates sit next to each other
        nums.sort()

        def backtracking(index, path):
            if index == len(nums):
                result.append(path[:])
                return
            
            # 2. Left Choice: Include the current number
            path.append(nums[index])
            backtracking(index + 1, path)
            
            # 3. Cleanse
            path.pop()
            
            # 4. Right Choice: Skip all identical copies of this number
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
                
            backtracking(index + 1, path)

        backtracking(0, [])
        return result
