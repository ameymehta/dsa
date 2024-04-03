def findMaxSumOfArr(k, arr):
  maxSum, windowStart, windowSum = 0, 0, 0
  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]
    if(windowEnd >= k-1):
      maxSum = max(maxSum, windowSum)
      windowSum -= arr[windowStart]
      windowStart += 1
  return maxSum

def main():
  print("Maximum sum of a subarray of size K: " + str(findMaxSumOfArr(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(findMaxSumOfArr(2, [2, 3, 4, 1, 5])))

main()
