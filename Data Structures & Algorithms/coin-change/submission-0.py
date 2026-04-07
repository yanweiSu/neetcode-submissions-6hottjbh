class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Define dp[n] as the fewest number of coins to get n
        # Then dp[n] = 1 + min_c{dp[n-coins[c]]}
        # dp[0]=0; dp[<0]=-infty
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for n in range(1, amount + 1):
            for c in coins:
                if c <= n:
                    dp[n] = min(1 + dp[n-c], dp[n])


        return dp[amount] if dp[amount] < INF else -1
