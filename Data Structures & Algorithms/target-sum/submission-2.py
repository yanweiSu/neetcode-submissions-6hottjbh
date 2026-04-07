class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # value v, nums index n
        # dp[v, n] = dp[v-nums[n], n-1] + dp[v+nums[n], n-1]
        # dp[nums[0], 0] = dp[-nums[0], 0] = 1, otherwise 0
        # MAX = sum of nums, MIN = -MAX
        MAX = 0
        for n in nums:
            MAX += n
        MIN = -MAX

        # dp = [[0] * len(nums)] * (2 * MAX)
        dp = [[0] * len(nums) for _ in range(2*MAX+1)]
        dp[MAX + nums[0]][0] += 1
        dp[MAX - nums[0]][0] += 1
        for i in range(1, len(nums)):
            for j in range(2 * MAX + 1):
                if j >= nums[i]:
                    dp[j][i] += dp[j-nums[i]][i-1]
                if j + nums[i] <= 2*MAX:
                    dp[j][i] += dp[j+nums[i]][i-1]

        return dp[MAX + target][len(nums)-1] if target <= MAX and target >= -MAX else 0
