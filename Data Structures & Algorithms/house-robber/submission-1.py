class Solution:
    def rob(self, nums: List[int]) -> int:
        # if only one house then its amount itself is the max we can rob 
        if len(nums) == 1:
            return nums[0]
        
        # similar to prev make an array for storing stuff of n+1 length 
        # tbh n+1 not needed if we assume from 0 its upon us 
        dp = [0]*(len(nums))
        # in prev problem dp was the no of ways but here it is the total amount
        # dp changes problem to problem its not something fixed  

        # now to get the base cases 
        # as for robbing only one house we get only that house's money 
        dp[0] = nums[0]
        # as for second house, we choose bw the first and this one depending which 
        # has more money as we cant choose both adjacent ones 
        dp[1] = max(nums[0], nums[1])

        # as for choosing to take or skip an house , is we skip it then we get amt 
        # from last adj house(i-1) if we take it we get this house's money + 
        # the money from house 2 behind from here (nums[i]+dp[i-2])
        # and obv we choose max from both 
        for i in range(2, len(nums)):
            dp[i] = max((nums[i] + dp[i-2]), dp[i-1])
        return dp[-1]
        # obv we return money we'd have accumilated till we reach the last house 
        # as that would be the final value of our loot 

 