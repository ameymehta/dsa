import re

def reverse_words_in_string(sentence):
    sentence = re.sub(' +', ' ', sentence.strip())
    sentence = list(sentence)
    len_sentence = len(sentence)
    reverse_chars(sentence, 0, len_sentence-1)
    start = 0
    for end in range(len_sentence + 1):
        if end == len_sentence or sentence[end] == ' ':
            reverse_chars(sentence, start, end - 1)
            start = end + 1
    return ''.join(sentence)



def reverse_chars(sentence, start, end):
    while start <= end:
        sentence[start], sentence[end] = sentence[end], sentence[start]
        start += 1
        end -= 1


def main():
    string_to_reverse = ["Hello World",
                        "a   string   with   multiple   spaces",
                        "Case Sensitive Test 1234",
                        "a 1 b 2 c 3 d 4 e 5",
                        "     trailing spaces",
                        "case test interesting an is this"]
    
    for i in range(len(string_to_reverse)):
        print('-----')
        print('Input for case ' + str(i))
        print(string_to_reverse[i])
        output = reverse_words_in_string(string_to_reverse[i])
        print('Output for case ' + str(i))
        print(output)

main()