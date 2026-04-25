"""
https://codesignal.com/blog/example-codesignal-questions/

You are given two strings: pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

Your task is to calculate the number of substrings of source that match pattern. 

We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
– The pattern and substring are equal in length.
– Where there is a 0 in the pattern, there is a vowel in the substring. 
– Where there is a 1 in the pattern, there is a consonant in the substring. 

Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.

Example

For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.
– “010” matches source[0..2] = "ama". The pattern specifies “vowel, consonant, vowel”. “ama” matches this pattern: 0 matches a, 1 matches m, and 0 matches a. 
– “010” doesn’t match source[1..3] = "maz" 
– “010” matches source[2..4] = "azi" 
– “010” doesn’t match source[3..5] = "zin" 
– “010” doesn’t match source[4..6] = "ing"

So, there are 2 matches. For a visual demonstration
"""

def match_the_pattern(pattern, source):
    matches = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in range(len(source) - len(pattern) + 1):
        matches += matcher(pattern, source, vowels, i)
    return matches

def matcher(pattern, source, vowels, i):
    for p in pattern:
        if p == '0':
            if source[i] not in vowels:
                return 0
        if p == '1':
            if source[i] in vowels:
                return 0
        i += 1
    return 1

match_the_pattern("010", "amazing")
