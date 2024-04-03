def find_word_concatenation(st, words):
    result_indices = []
    if len(words) == 0 or len(words[0]) == 0:
        return result_indices

    num_of_words = len(words)
    len_of_word = len(words[0])
    len_of_concat = num_of_words * len_of_word
    if len(st) < len_of_concat:
        return result_indices

    word_map = {}
    for word in words:
        if word not in word_map:
            word_map[word] = 0
        word_map[word] += 1

    for i in range(len(st) - len_of_concat + 1):
        words_visited = {}
        for j in range(num_of_words):
            next_word_index = i + (j * len_of_word)
            word = st[next_word_index:next_word_index + len_of_word]
            # print(word)
            if word not in word_map:
                break

            if word not in words_visited:
                words_visited[word] = 0
            words_visited[word] += 1

            if words_visited[word] > word_map[word]:
                break

            if j + 1 == num_of_words:
                result_indices.append(i)

    return result_indices


def main():
    st = "catfoxcat"
    words = ["cat", "fox"]
    print(find_word_concatenation(st, words))
    st = "catcatfoxfox"
    words = ["cat", "fox"]
    print(find_word_concatenation(st, words))


main()
