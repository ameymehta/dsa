def justify(current, count, maxWidth):
    if len(current) == 1:
        for i in range(maxWidth - count):
            current[0] += ' '
        return current[0]
    else:
        for i in range(maxWidth - count):
            current[i % (len(current)-1)] += ' '
        return ''.join(current)


def fullJustify(words, maxWidth):
    result, current, count = [], [], 0
    for word in words:
        if len(word) + count + len(current) > maxWidth:
            result.append(justify(current, count, maxWidth))
            current, count = [], 0
        current.append(word)
        count += len(word)
    result.append(" ".join(current) + " "*(maxWidth - len(current) - count + 1))
    return result


def main():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    res = fullJustify(words, maxWidth)
    print(res)


main()

# ["What   must   be","acknowledgment  ","shall be        "]
# ['This    is    an', 'example  of text', 'justification.  ']