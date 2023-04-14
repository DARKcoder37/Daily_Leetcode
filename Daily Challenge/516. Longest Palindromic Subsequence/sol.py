# 1) Top down

class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    # dp(i, j) := LPS's length in s[i..j]
    @functools.lru_cache(None)
    def dp(i: int, j: int) -> int:
      if i > j:
        return 0
      if i == j:
        return 1
      if s[i] == s[j]:
        return 2 + dp(i + 1, j - 1)
      return max(dp(i + 1, j), dp(i, j - 1))

    return dp(0, len(s) - 1)

# 2) Bottom up

class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    n = len(s)
    # dp[i][j] := LPS's length in s[i..j]
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
      dp[i][i] = 1

    for d in range(1, n):
      for i in range(n - d):
        j = i + d
        if s[i] == s[j]:
          dp[i][j] = 2 + dp[i + 1][j - 1]
        else:
          dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]