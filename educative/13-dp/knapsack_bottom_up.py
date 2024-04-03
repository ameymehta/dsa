def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or n != len(weights):
        return 0

    dp = [[0 for col in range(capacity + 1)] for row in range(n)]

    # 0 capcacity column already have 0 profits

    # for first wight, its only one weight, so we populate it
    for cap in range(1, capacity + 1):
        if weights[0] <= cap:
            dp[0][cap] = profits[0]

    for i in range(1, n):
        for cap in range(1, capacity + 1):
            profit1 = 0
            if weights[i] <= cap:
                profit1 = profits[i] + dp[i-1][cap-weights[i]]
            profit2 = dp[i-1][cap]
            dp[i][cap] = max(profit1, profit2)

    return dp[n-1][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
