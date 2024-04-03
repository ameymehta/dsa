def can_partition(num):
    s = sum(num)
    if s % 2 != 0:
        return False
    dp = [[-1 for col in range(int(s/2) + 1)] for row in range(len(num))]
    return True if can_partition_recursive(dp, num, s/2, 0) == 1 else False


def can_partition_recursive(dp, num, sum, currentIndex):
    # base check
    if sum == 0:
        return 1

    if(currentIndex >= len(num)):
        return 0

    if dp[currentIndex][sum] == -1:
        if(num[currentIndex] <= sum):
            if can_partition_recursive(dp, num, sum-num[currentIndex], currentIndex+1) == 1:
                dp[currentIndex][sum] = 1
                return 1

        dp[currentIndex][sum] = can_partition_recursive(
            dp, num, sum, currentIndex+1)

    return dp[currentIndex][sum]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
