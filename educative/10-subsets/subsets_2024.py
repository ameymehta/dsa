def find_subsets(ss):
    result = []
    result.append([])
    for e in ss:
        curLen = len(result)
        for i in range(curLen):
            cur = list(result[i])
            cur.append(e)
            result.append(cur)
    return result


def main():
    print("Here is the list of subsets: " + str(find_subsets(['A', 'B'])))
    print("Here is the list of subsets: " + str(find_subsets(['A', 'B', 'C'])))


main()
