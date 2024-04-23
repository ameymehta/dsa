# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# loop through words
# add word to current array (after if)
# add len(word) to num_of_letters (after if)
# check if num_of_letters + len(word) + len(crrrent) > max_width
# take white spaces to be added, distribute them among all words but last
# concat all in current array, append to result

def justifyLine(current_line, maxWidth, count):
    if len(current_line) == 1:
        for i in range(maxWidth - count):
            current_line[0] += " "
        return current_line[0]
    else:
        for i in range(maxWidth - count):
            current_line[i % (len(current_line) - 1)] += " "
        return "".join(current_line)
    
def justifyLastLine(current_line, maxWidth, count):
    i = 0
    while i < (maxWidth - count - 1) and i < len(current_line) - 1:
        current_line[i % (len(current_line) - 1)] += " "
        i += 1
    while i < (maxWidth - count - 1):
        current_line[len(current_line) - 1] += " "
        i += 1
    return "".join(current_line)
    

def fullJustify(words, maxWidth):
    result = []
    count = 0
    current_line = []
    for word in words:
        if len(word) + count + len(current_line) >= maxWidth:
            justifiedLine = justifyLine(current_line, maxWidth, count)
            result.append(justifiedLine)
            current_line = []
            count = 0
        current_line.append(word)
        count += len(word)
    justifiedLastLine = justifyLastLine(current_line, maxWidth, count)
    result.append(justifiedLastLine)
    return result

def main():
    words = ["This", "is", "an", "example", "of", "text", "just", "ify"]
    maxWidth = 16
    res = fullJustify(words, maxWidth)
    print(res)

    words2 = ["What","must","be","acknowledgment","shall","be"]
    maxWidth2 = 16
    res2 = fullJustify(words2, maxWidth2)
    print(res2)

    words3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth3 = 20
    res3 = fullJustify(words3, maxWidth3)
    print(res3)

main()
