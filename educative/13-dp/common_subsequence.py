def find_LCS_length(s1, s2):
    return find_LCS_recursive(s1, s2, 0, 0)


def find_LCS_recursive(s1, s2, i1, i2):
    if i1 >= len(s1) or i2 >= len(s2):
        return 0

    if s1[i1] == s2[i2]:
        return 1 + find_LCS_recursive(s1, s2, i1 + 1, i2 + 1)

    c1 = find_LCS_recursive(s1, s2, i1 + 1, i2)
    c2 = find_LCS_recursive(s1, s2, i1, i2 + 1)
    return max(c1, c2)


def main():
    print(find_LCS_length("abdca", "cbda"))
    print(find_LCS_length("passport", "ppsspt"))


main()
