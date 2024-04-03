def is_palindrome(s):
    left = 0
    right = len(s) -1
    while (left < right):
        if (left != right):
            return False
        left += 1
        right -= 1
    return True


# Driver Code
def main():

    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("Input: '", test_cases[i], "'. String length: ", len(test_cases[i]), ".", sep='')
        print("Is it a palindrome? ", is_palindrome(test_cases[i]))


if __name__ == '__main__':
    main()