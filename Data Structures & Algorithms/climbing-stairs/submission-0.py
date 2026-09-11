class Solution:
    def climbStairs(self, n: int) -> int:
        # for 1 step  only 1 way which is itself 
        # for 2 steps steps, 2 ways => 1 + 1 or directly 2 
        if n <= 2:
            return n 
        # for more than 2 ways itll be a combn of these base cases , so the whole 
        # idea is to store for each instead of calculating everytime for each index
        # we create ann array with 6 places as n = 5 , so that we can directly acces
        # dp[5] index representing the number of ways of getting to the 5th stair 
        # or no of ways of getting 5 from the given base cases , so 
        dp = [0]*(n+1)
        # after creation of array just putthe given base case values 
        dp[1] , dp[2] = 1, 2 
        # [0 , 1, 2, 0 ,0, 0 , 0]
        #  0   1  2  3  4  5   6
        for i  in range(3, n+1): #will go till 5 only
            # now we basically just fill the array with our genaralized formula
            dp[i] = dp[i-1] + dp[i-2]
            # we actually can observe it ex = 3 stairs  = 1 + 1 + 1 or 
            #  1+ 2 or 2+1 , so dp[3] = 3 = 1+2 = no of ways of 1 + no of ways of 2
        return dp[n]


