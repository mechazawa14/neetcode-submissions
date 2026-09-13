class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # making the dp array like we did till now to store them variables 
        # here in this problem dp[i] is the length of longest increasing sequence 
        # ending with i 
        dp = [1]*len(nums)
        # [1] instead of [0] as a single number itself is of a size 1 sequence 

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i] , dp[j]+1)
        return max(dp)

        