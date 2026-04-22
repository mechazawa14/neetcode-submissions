class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic= {}
        for i in range (len(nums)):
            compliment = target - nums[i]
            if compliment in dic :
                return [dic[compliment], i]
            else :
                dic[nums[i]] = i
        return None 