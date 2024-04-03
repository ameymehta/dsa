def longest_substring_with_k_distinct(str, k):
    max_len = 0
    window_start = 0
    char_freq = {}
    for window_end in range(len(str)):
        right_ch = str[window_end]
        if right_ch not in char_freq:
            char_freq[right_ch] = 0
        char_freq[right_ch] += 1

        while len(char_freq) > k:
            left_ch = str[window_start]
            char_freq[left_ch] -= 1
            if char_freq[left_ch] == 0:
                del char_freq[left_ch]
            window_start += 1
        
        max_len = max(max_len, window_end-window_start+1)
    return max_len


def main():
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
