class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp= [0] * (n+2)
        # aim is to reach index + 1 th stair where index = max index in cost, so n+2 
        # let now dp[i] = minimum cost required to REACH position i

    # clearly say were at a particular step , we clearly came to it from either last 
    # step or last 2nd step as told that we can go to either i+1 or i+2 th floor 
    # so dp[step] = min(cost already till i+1 th step + cost[i+1](from there to current step), cost already till i+2 the step + cost[i+2](from there to current))
    # making base case , most basic initial subproblems to kickstart the loop
        dp[0] = 0
        dp[1] = 0 #as tiold we can start at either index 0 or index 1 
        dp[2] = min(cost[0], cost[1]) #we can come to 2 from either 0th step or 1st step 
        # time to make the dp now 
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+cost[i-2])
        return dp[n]
            
             
