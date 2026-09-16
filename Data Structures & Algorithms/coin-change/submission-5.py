class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount + 1)

        dp[0]=  0 

        if len(coins) == 1 and amount != coins[0] and amount%coins[0] == 0:
            return amount//coins[0]
        if len(coins) == 1 and amount != coins[0] and amount%coins[0] != 0:
            return -1 
        if len(coins) == 1 and amount != coins[0]:
            return -1 

        
        for i in range(len(dp)):
            for coin in coins :
                if coin <= i :
                    dp[i]= min(dp[i], dp[i-coin]+1)
        if dp[amount] == amount+ 1 :
            return -1 

        return dp[amount]
