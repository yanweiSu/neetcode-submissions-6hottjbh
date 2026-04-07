class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            # calculate dp[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])

        maxval = 0
        for i in range(len(dp)):
            maxval = max(dp[i], maxval)

        return maxval