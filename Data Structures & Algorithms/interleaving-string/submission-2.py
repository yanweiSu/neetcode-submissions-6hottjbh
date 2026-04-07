class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i, j]: s3[:i+j] is from s1[:i] and s2[:j]
        # dp[i, j] = ((s1[i-1] == s3[i+j-1]) & dp[i-1][j]) or ((s2[j-1] == s3[i+j-1]) & dp[i][j-1])
        # dp[0, j] is true if s3[:j] == s2[:j]
        # dp[i, 0] is true if s3[:i] == s1[:i]

        if len(s3) != len(s1) + len(s2):
            return False

        dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
        # dp[i, j] = s3[:i+j] can be made from s1[:i] and s2[:j]
        # so i = 1..len(s1) and j = 1..len(s2)
        dp[0][0] = 1   # dp[0, 0] = True
        for i in range(1, len(s1)+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = 1
            else:
                break
        for j in range(1, len(s2)+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = 1
            else:
                break
        
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = ((s1[i-1] == s3[i+j-1]) and dp[i-1][j]) or ((s2[j-1] == s3[i+j-1]) and dp[i][j-1])

        return bool(dp[len(s1)][len(s2)])
