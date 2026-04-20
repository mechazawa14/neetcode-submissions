class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps= {}
        for i in range (len(nums)):
            compliment  = target - nums[i]
            if compliment in comps :
                return [comps[compliment],i]
            else :
                comps[nums[i]]= i 
        return None 