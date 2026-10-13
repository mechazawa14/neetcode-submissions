class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numa = set(nums)
        if len(numa) != len(nums):
            return True 
        return False