import math

def smallesSubarrayWithGivenSum(s, arr):
  minLength = math.inf
  windowSum = 0
  windowStart = 0
  for windowEnd in range(0, len(arr)):
    windowSum += arr[windowEnd]
    while(windowSum >= s):
      minLength = min(minLength, windowEnd - windowStart + 1)
      windowSum -= arr[windowStart]
      windowStart += 1
  if(minLength == math.inf):
    return 0
  return minLength

def main():
  print("Smallest subarray length: " + str(smallesSubarrayWithGivenSum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallesSubarrayWithGivenSum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallesSubarrayWithGivenSum(8, [3, 4, 1, 1, 6])))


main()
