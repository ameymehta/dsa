from collections import deque


def find_subsets(elements):
    subsets = []
    subsets.append([])
    for e in elements:
        subsets_size = len(subsets)
        for i in range(subsets_size):
            current_set = list(subsets[i])
            current_set.append(e)
            subsets.append(current_set)
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets(['A', 'B'])))
    print("Here is the list of subsets: " + str(find_subsets(['A', 'B', 'C'])))


main()
