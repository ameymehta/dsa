def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for i in range(len(profits))] for j in range(capacity + 1)]
    return solve_knapsack_recursive(dp, profits, weights, capacity, 0)


def solve_knapsack_recursive(dp, profits, weights, capacity, currentIndex):
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    if dp[capacity][currentIndex] != -1:
        return dp[capacity][currentIndex]

    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + solve_knapsack_recursive(
            dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    profit2 = solve_knapsack_recursive(
        dp, profits, weights, capacity, currentIndex + 1)

    dp[capacity][currentIndex] = max(profit1, profit2)

    return dp[capacity][currentIndex]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
