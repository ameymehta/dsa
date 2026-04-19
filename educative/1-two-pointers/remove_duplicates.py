def remove_duplicates(arr):
  non_dup_tracker = 0
  for i in range(1, len(arr)):
    if arr[non_dup_tracker] != arr[i]:
      arr[non_dup_tracker + 1] = arr[i]
      non_dup_tracker += 1
  return non_dup_tracker + 1

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()
