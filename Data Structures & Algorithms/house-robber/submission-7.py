class Solution:
    def rob(self, nums: List[int]) -> int:
            # 1. visualize , so ive got a string of houses which i need to rob 
            # 2. the subproblem here might be , hmm how bout , how tf we even gonna start 
            # see if im not wrong , len(nums) will be the number of houses weve got to rob 
            # and now the base problem would be to atleast start so 
            # money accumulated from robbing first house = nums[0], theres no choice to be made , and money accumulated after robbing second house would mean i havent robbed the first house in the first place so .... how about we say let dp[i]= money accumulated from robbing a house , where len(dp) = len(nums) which is the number of houses 
            # seems like we gotta make the base cases here like 
            # dp[0] = nums[0] and dp[1] = max(dp[0] , nums[1]) as we would choose more 
            # so the relationship is starting to form like 
            # dp[i] = max(dp[i-1], dp[i-2] + nums[i]) which is really is just a choice between if we skip the prev one or if we take the prev one depending on in which case we get more money 
            if len(nums) ==  1 :
                return nums[0]
            if len(nums) <= 2 :
                return max(nums[0], nums[1])
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(dp[0] , nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return max(dp)