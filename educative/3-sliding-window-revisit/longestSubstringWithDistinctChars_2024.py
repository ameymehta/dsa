def longestSubstringWithDistinctChars(str1, k):
  start = 0
  len_str = len(str1)
  max_length = 0
  char_freq = {}
  for end in range(len_str-1):
    right_char = str1[end]
    if(right_char not in char_freq):
      char_freq[right_char] = 0
    char_freq[right_char] += 1

    while(len(char_freq) > k):
      left_char = str1[start]
      char_freq[left_char] -= 1
      if char_freq[left_char] == 0:
        del char_freq[left_char]
      start += 1
      
    max_length = max(max_length, end - start + 1)

  return max_length

def main():
  print("Length of the longest substr1ing: " + str(longestSubstringWithDistinctChars("araaci", 2)))
  print("Length of the longest substr1ing: " + str(longestSubstringWithDistinctChars("araaci", 1)))
  print("Length of the longest substr1ing: " + str(longestSubstringWithDistinctChars("cbbebi", 3)))


main()
