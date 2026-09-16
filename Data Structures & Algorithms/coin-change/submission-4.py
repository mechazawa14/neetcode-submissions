class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #to visualize one thing is important say i gotta make amt of 12 then say i got coins 1 5 and 10 , it would be clear to say that if i use a coin of 5 rs then i gotta need a way to make 12 - 5 = 7 so  id say i need 1 (already taken 5) + coins to make 7  so for every coin and amt combo , the total coins needed are 1(coin itself) + coins for remaining amt sum , so thats the basic idea for subproblems as well 
        # making the relation ship as told prev , lets make dp first , basically lets say oo make amt we d at max need amount number of coins which is using the one coin i suppose , so for that reason u get urself in dp amt number of boxes but given the fact that we start from 0 index its more convinient to make amt + 1 boxes as it would mean ill get the last index as the exact amount i need so 
        dp = [amount+1]*(amount+1)
        # amount + 1 is used as a safe impossibly large value in array 
        dp[0]= 0 #as we need 0 coins to make a sum of 0 
        # now we try every coin amt combo 

        # befroe that one little edge cases
        if amount == 0 :
            return 0
        if len(coins)==1 and coins[0]!= amount and amount%coins[0] !=0 :
            return -1 
        for i in range(1, len(dp)):
            for coin in coins :
                if coin <= i: #as i - coin better not be negative 
                    dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
