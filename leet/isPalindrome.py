def isPalindrome(s):
    alnum = []
    for i in range(len(s)):
        if s[i].isalnum():
            alnum.append(s[i])

    print(alnum)

    l = 0
    r = len(alnum) - 1

    while l <= r:
        if alnum[l].lower() != alnum[r].lower():
            return False
        l += 1
        r -= 1

    return True


def main():
    print(isPalindrome('A man, a plan, a canal: Panama'))


main()
