def find_LPS_length(str):
  n = len(str)
  dp = [[False for c in range(n)] for r in range(n)]
  for i in range(n):
    dp[i][i] = True
  maxLen = 1
  for startInd in range(n-1, -1, -1):
    for endInd in range(startInd+1, n):
      if str[startInd] == str[endInd]:
        if endInd-startInd==1 or dp[startInd+1][endInd-1]:
          dp[startInd][endInd] = True
          maxLen = max(maxLen, endInd-startInd+1)
  
  return maxLen

def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()
