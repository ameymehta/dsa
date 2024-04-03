def avg_of_sub_arrays(k, arr):
    windowSum = 0.0
    windowStart = 0
    result = []
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if(windowEnd >= k - 1):
            result.append(windowSum/k)
            windowSum -= arr[windowStart]
            windowStart += 1
        
    return result

def main():
  result = avg_of_sub_arrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))

main()