def find_LCS_length(s1, s2):
  n1, n2 = len(s1), len(s2)
  dp = [[0 for c in range(n2+1)] for r in range(n1+1)]
  maxLen = 0
  for i in range(1, n1+1):
    for j in range(1, n2+1):
      if s1[i-1] == s2[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
        maxLen = max(maxLen, dp[i][j])
  return maxLen


def main():
  print(find_LCS_length("abdca", "cbda"))
  print(find_LCS_length("passport", "ppsspt"))


main()