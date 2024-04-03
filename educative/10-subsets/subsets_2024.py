def find_subsets(ss):
    result = []
    result.append([])
    for e in ss:
        cur_len = len(result)
        for i in range(cur_len):
            cur_set = list(result[i])
            cur_set.append(e)
            result.append(cur_set)
    return result


def main():
    print("Here is the list of subsets: " + str(find_subsets(['A', 'B'])))
    print("Here is the list of subsets: " + str(find_subsets(['A', 'B', 'C'])))


main()
