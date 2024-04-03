# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# loop through words
# add word to current array (after if)
# add len(word) to num_of_letters (after if)
# check if num_of_letters + len(word) + len(crrrent) > max_width
# take white spaces to be added, distribute them among all words but last
# concat all in current array, append to result

def justify(maxWidth, current, count):
    if len(current) == 1:
        for i in range(maxWidth - count):
            current[0] += " "
        return current[0]
    else:
        for i in range(maxWidth - count):
            current[i%(len(current) - 1)] += " "
        return "".join(current)

def fullJustify(words, maxWidth):
    # result[] holds justified lines
    # current[] holds words for the current line
    # count is counter for number of chars so far
    result, current, count = [], [], 0
    for word in words:
        if len(word) + count + len(current) > maxWidth:
            result.append(justify(maxWidth, current, count))
            current, count = [], 0
        current.append(word)
        count += len(word)
    result.append(justify(maxWidth, current, count))
    return result

def main():
    words = ["This", "is", "an", "example", "of", "text", "just", "ify"]
    maxWidth = 16
    res = fullJustify(words, maxWidth)
    print(res)

main()
