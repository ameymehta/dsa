def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    start, end = 0, 0
    min_len = float('inf')
    result = ""
    char_freq = {}
    win_freq = {}
    formed = 0
    for ch in t:
        if ch not in char_freq:
            char_freq[ch] = 0
        char_freq[ch] += 1

    while end < len(s):
        r_ch = s[end]
        if r_ch not in win_freq:
            win_freq[r_ch] = 0
        win_freq[r_ch] += 1
        if r_ch in t and win_freq[r_ch] == char_freq[r_ch]:
            formed += 1
        while formed == len(char_freq):
            win_len = end - start + 1
            if win_len <= min_len:
                min_len = win_len
                result = "".join(s[start:end+1])
            l_ch = s[start]
            start += 1
            win_freq[l_ch] -= 1
            if l_ch in t and win_freq[l_ch] < char_freq[l_ch]:
                formed -= 1
        end += 1
    return result


def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t))


main()
