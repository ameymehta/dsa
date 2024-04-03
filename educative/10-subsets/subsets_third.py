def find_subsets(elements):
    subsets = []
    subsets.append([])
    for element in elements:
        currentsize = len(subsets)
        for i in range(currentsize):
            currentset = list(subsets[i])
            currentset.append(element)
            subsets.append(currentset)
    return subsets



def main():

    print("Here is the list of subsets: " + str(find_subsets(['A', 'B'])))
    print("Here is the list of subsets: " + str(find_subsets(['A', 'B', 'C'])))


main()
