def non_repeat_substring(str1):
    start = 0
    maxlen = 0
    char_map = {}

    for end in range(len(str1)):
        right_char = str1[end]
        if right_char in char_map:
            start = max(start, char_map[right_char] + 1)
        char_map[right_char] = end
        maxlen = max(maxlen, end - start + 1)

    return maxlen


def main():
    print("Length of the longest substring: " +
          str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abccde")))


main()
