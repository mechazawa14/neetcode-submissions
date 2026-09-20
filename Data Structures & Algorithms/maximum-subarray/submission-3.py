class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0 
        if len(nums)== 1:
            return nums[0]
        # 1. what is choice : the choice is to select an element from array 
        # maxsumset  = [] or directly lets just keep an incrementing variable 
        currentsum  = 0 
        bestsum  = 0
        for i in range(len(nums)):
            # 2. local choice 
            currentsum += nums[i]
            bestsum = max(bestsum , currentsum)
            # 3. consequences of this choice and act according to it 
            if currentsum < 0 :
                currentsum = 0 

        positivefound = 0
        for i in nums :
            if i > 0:
                positivefound = 1
        if positivefound == 0:
            return max(nums)
        return bestsum


            