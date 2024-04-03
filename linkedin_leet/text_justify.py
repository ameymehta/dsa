# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# loop through words
# add word to current array (after if)
# add len(word) to num_of_letters (after if)
# check if num_of_letters + len(word) + len(crrrent) > max_width
# take white spaces to be added, distribute them among all words but last
# concat all in current array, append to result


def fullJustify(self, words, maxWidth):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i%(len(cur)-1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(maxWidth)]