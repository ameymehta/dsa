def length_of_longest_substring(str, k):
    window_start, max_length, max_freq = 0, 0, 0
    char_freq = {}
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
        max_freq = max(max_freq, char_freq[right_char])
        if (window_end-window_start+1-max_freq) > k:
            left_char = str[window_start]
            char_freq[left_char] -= 1
            window_start += 1
        max_length = max(max_length, window_end-window_start+1)
    return max_length


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
