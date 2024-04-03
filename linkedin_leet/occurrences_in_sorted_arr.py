def occurrences_in_sorted_arr(arr, target):
  left = binary_search(arr, target, True)
  if left < 0:
    return 0
  right = binary_search(arr, target, False)
  return right - left + 1

def binary_search(arr, target, leftmost):
  lo, hi, i = 0, len(arr)-1, -1
  while lo <= hi:
    mid = (lo + hi)//2
    if target > arr[mid]:
      lo = mid + 1
    elif target < arr[mid]:
      hi = mid - 1
    else:
      i = mid
      if leftmost:
        hi = mid - 1
      else:
        lo = mid + 1
  return i

def main():
  arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42]
  target = 8
  print occurrences_in_sorted_arr(arr, target)
  arr = [3, 5, 5, 5, 5, 7, 8, 8]
  target = 6
  print occurrences_in_sorted_arr(arr, target)
  arr = [3, 5, 5, 5, 5, 7, 8, 8]
  target = 5
  print occurrences_in_sorted_arr(arr, target)

main()
