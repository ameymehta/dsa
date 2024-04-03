def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for c in range(capacity+1)] for r in range(len(profits))]
    return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, currentIndex):
    # base check (capacity<=0 or currentIndex >= len(profits))
    if(capacity <= 0 or currentIndex >= len(profits)):
        return 0

    # if problem already solved, return from memo
    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]

    # 1st profit including the currentIndex (check if weight<=capacity)
    profit1 = 0
    if(weights[currentIndex] <= capacity):
        profit1 = profits[currentIndex] + knapsack_recursive(
            dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    # 2nd profit excluding the currentIndex
    profit2 = knapsack_recursive(
        dp, profits, weights, capacity, currentIndex + 1)

    # memoize max(1st,2nd) and return memo
    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
