def find_LPS_length(st):
    n = len(st)
    dp = [[False for col in range(n)] for row in range(n)]
    for i in range(n):
        dp[i][i] = True
    maxlen = 1
    for start_i in range(n-1, -1, -1):
        for end_i in range(start_i + 1, n):
            if st[start_i] == st[end_i]:
                if end_i - start_i == 1 or dp[start_i + 1][end_i - 1]:
                    dp[start_i][end_i] = True
                    maxlen = max(maxlen, end_i - start_i + 1)
    return maxlen


def main():
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))


main()
