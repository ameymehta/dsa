def pair_with_target_sum(arr, target_sum):
  left = 0
  right = len(arr)-1
  while left < right:
    if arr[left] + arr[right] == target_sum:
      return [left, right]
    elif arr[left] + arr[right] < target_sum:
      left += 1
    else:
      right -= 1
  return [-1, -1]

def main():
  print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
  print(pair_with_target_sum([2, 5, 9, 11], 11))


main()
