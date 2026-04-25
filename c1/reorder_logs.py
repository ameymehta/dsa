"""
https://www.finalroundai.com/blog/top-10-capital-one-code-signal-questions-you-should-prepare-for

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
Letter-logs are sorted lexicographically by their contents. If their contents are the same, sort by identifier.
Digit-logs maintain their relative ordering.
Example: For logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]:

The output should be ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"].

Explanation:

Letter-logs: "let1 art can", "let2 own kit dig", "let3 art zero"
Sorted by content: "art can" < "art zero" < "own kit dig"
"art can" and "art zero" both start with "art", so sort by identifier: let1 < let3
Digit-logs maintain order: "dig1 8 1 5 1", "dig2 3 6"
This is not algorithmically complex but it's a good test of your ability to parse requirements and implement custom comparators correctly. You need to understand stable sorting, string manipulation, and how to create proper sort keys. This tests attention to detail and the ability to handle multiple sorting criteria.
"""


def sort_logs(logs):
    letter_logs = []
    digi_logs = []

    for log in logs:
        iden, rest = log.split(' ', 1)
        if rest[0].isalpha():
            letter_logs.append((rest, iden, log))
        else:
            digi_logs.append((rest, iden, log))

    letter_logs.sort(key=lambda x:(x[0], x[1]))

    result = []
    for ll in letter_logs:
        result.append(ll[2])
    for dl in digi_logs:
        result.append(dl[2])

    return result

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(sort_logs(logs))
# Output: ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

