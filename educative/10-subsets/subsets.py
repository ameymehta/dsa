def find_subsets(elements):
    subsets = []
    subsets.append([])
    for element in elements:
        n = len(subsets)
        for i in range(n):
            set = list(subsets[i])
            set.append(element)
            subsets.append(set)
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets(['A', 'B'])))
    print("Here is the list of subsets: " + str(find_subsets(['A', 'B', 'C'])))


main()
