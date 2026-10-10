class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. visualize 
        # 2. identify the subproblem 
        # dp[i] let dep be the total no of ways to reach a stair i
        if n<=2 :
            return n
        # 3. find the relationship 
        dp = [0]*(n+1)
        dp[1], dp[2] = 1, 2

        # 4. generalize 
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
