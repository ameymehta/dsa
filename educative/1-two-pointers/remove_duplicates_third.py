def remove_duplicates(arr):
  next_non_duplicate = 0
  for i in range(1, len(arr)):
    if arr[next_non_duplicate] != arr[i]:
      arr[next_non_duplicate + 1] = arr[i]
      next_non_duplicate += 1
  
  print(arr)
  return next_non_duplicate + 1

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()
