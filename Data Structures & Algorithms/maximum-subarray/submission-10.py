class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0 
        if len(nums)==1 :
            return nums[0]
        bestsumyet = 0
        currentsum = 0

        for i in range(len(nums)):
            currentsum += nums[i] 
            bestsumyet = max(currentsum, bestsumyet)

            if currentsum < 0:
                currentsum = 0 
    
        positivefound = 0
        for i in nums :
            if i > 0:
                positivefound = 1
        if positivefound == 0:
            return max(nums)

        return bestsumyet

        # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        # lists like these is the reason we have this line 
         # bestsumyet = max(currentsum, bestsumyet)
        #  had we not had that line and simply returned currentsum then our output would be 5 but ans is 6 

