class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                mune=nums[i]+nums[j]
                if mune==target:
                    return [i,j]
        return []
                
