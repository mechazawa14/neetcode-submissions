class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments  = {}
        for i in range(len(nums))  :
            compliment  = target  - nums[i]
            if compliment in compliments :
                # return list(compliments[compliment], nums.index(i))
                # list()expects only one argument in it to be listified
                return [compliments[compliment], i]
            else:
                compliments[nums[i]] = i
        return []

        