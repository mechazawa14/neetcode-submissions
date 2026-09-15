class Solution:
    def rob(self, nums: List[int]) -> int:
        # just simple lol , do the same as prev usual house robber 1 problem but once include start elem and exclude last  , second time vice versa 

        if len(nums)== 0:
                return 0
        if len(nums) == 1:
                return nums[0]
        def linear_houserobber(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums)==2 :
                return max(nums[0], nums[1])
            dp = [0] * len(nums)
            dp[0], dp[1] = nums[0] , max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return max(dp)

        
        return max(linear_houserobber(nums[:-1]),
                    linear_houserobber(nums[1:]))