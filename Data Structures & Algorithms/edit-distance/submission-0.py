class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Consider code -> cdee, we have the following ways
        # 1. First cod -> cdee (so now is cdeee), and then remove the last 'e'
        # 2. First code -> cde, and then insert 'e'
        # 3. cod -> cde
        # Let dp[i, j] be the edit dist between word1[:i] and word2[:j]
        # dp[0, 0] = 0
        # dp[i, j] = min{dp[i-1, j] + 1(remove the i-th), 
        #                dp[i, j-1] + 1(add the j-th),
        #                dp[i-1, j-1] + 1(replace the i-th by the j-th)}

        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                minval = 10000
                if (i==0) and (j==0):
                    continue
                if i >= 1:
                    minval = min(minval, dp[i-1][j] + 1)
                if j >= 1:
                    minval = min(minval, dp[i][j-1] + 1)
                if (i >= 1) and (j >= 1):
                    tmp = 0 if word1[i-1]==word2[j-1] else 1
                    minval = min(minval, dp[i-1][j-1] + tmp)

                dp[i][j] = minval

        
        return dp[len(word1)][len(word2)]