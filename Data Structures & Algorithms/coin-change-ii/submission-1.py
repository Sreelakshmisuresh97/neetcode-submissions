class Solution:
    def change(self,amount: int, coins: list[int]) -> int:
    # dp[i] stores the number of ways to make up amount i
        dp = [0] * (amount + 1)
    
    # Base case: 1 way to make amount 0 (use no coins)
        dp[0] = 1
    
    # Outer loop: iterate through each coin one by one
        for coin in coins:
        # Inner loop: update all amounts from the coin value up to the target amount
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
            
        return dp[amount]