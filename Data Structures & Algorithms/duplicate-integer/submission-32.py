class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seta = set(nums)
        if len(seta)!= len(nums):
            return True 
        return False 