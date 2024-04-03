def find_permutation_in_string(str, pattern):
    window_start = 0
    matched = 0
    char_freq = {}
    for chr in pattern:
        if chr not in char_freq:
            char_freq[chr] = 0
        char_freq[chr] += 1
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched += 1
        if matched == len(char_freq):
            return True
        # keep the window size equal to patter size
        if window_end >= len(pattern)-1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1

    return False


def main():
    print('oidbcaf/abc: ' + str(find_permutation_in_string("oidbcaf", "abc")))
    print('odicf/dc: ' + str(find_permutation_in_string("odicf", "dc")))
    print('bcdxabcdy/bcdyabcdx: ' +
          str(find_permutation_in_string("bcdxabcdy", "bcdyabcdx")))
    print('aaacb/abc: ' + str(find_permutation_in_string("aaacb", "abc")))


main()
