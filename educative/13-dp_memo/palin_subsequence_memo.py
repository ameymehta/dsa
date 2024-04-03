def find_LPS_length(str):
  n = len(str)
  dp = [[0 for c in range(n)] for r in range(n)]
  for i in range(n):
    dp[i][i] = 1
  for startInd in range(n-1, -1, -1):
    for endInd in range(startInd+1, n):
      if str[startInd] == str[endInd]:
        dp[startInd][endInd] = 2 + dp[startInd+1][endInd-1]
      else:
        dp[startInd][endInd] = max(dp[startInd+1][endInd], dp[startInd][endInd-1])
  
  return dp[0][n-1]

def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()
