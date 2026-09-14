class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. visualize : 
        # clearly this problem sounds like a dp problem as its clearly made up of smaller 
        # sub problems like as in 1 step or 2 steps first 

        # 2. find the subrproblems first : wkt to climb 5 or 10 or any other larger steps
        # i will first need to find way to climb till 1 or 2 steps 
        # let dp[i] = no or ways to climb ith steps so dp[1] = 1 dp[2] = 2 (1+1 or direct2)

        if n <= 2 :
            return n 

        dp = [0]*(n+1)
        # making an array of length same as the max no of stairs asked to climb
        # creates array of indices 0 1 2 3 4
        dp[1],dp[2] = 1,2 

        # 3. find relationship, the fact that we have our smaller basic steps of length 
        # 1 and 2 , it means we can reach any destination step if were only 1 or 2 steps 
        # away so the relationship is dp[i] = dp[i-1]+dp[i-2]
        # we have generalized it hence too 
        for i in range (3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

