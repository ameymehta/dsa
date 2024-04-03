def find_LPS_length(st):
    return find_LPS_recursive(st, 0, len(st)-1)


def find_LPS_recursive(st, left, right):
    if left > right:
        return 0

    if left == right:
        return 1

    if st[left] == st[right]:
        remaining_length = right - left - 1
        if find_LPS_recursive(st, left+1, right-1) == remaining_length:
            return remaining_length + 2

    l1 = find_LPS_recursive(st, left+1, right)
    l2 = find_LPS_recursive(st, left, right-1)
    return max(l1, l2)


def main():
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))


main()
