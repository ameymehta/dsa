def non_repeat_substring(str):
    window_start = 0
    max_length = 0
    char_index_map = {}
    for window_end in range(len(str)):
        right_char = str[window_end]
        # if char already in the window, shrink the window to next of the char
        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)
        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end-window_start+1)
    return max_length


def main():
    print("Length of the longest substring: " +
          str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abccde")))


main()
