def find_subsets(elements):
    result = []
    result.append([])
    for element in elements:
        current_len = len(result)
        for i in range(current_len):
            current_set = list(result[i])
            current_set.append(element)
            result.append(current_set)
    return result



def main():
    print("Here is the list of subsets: " + str(find_subsets(['A', 'B'])))
    print("Here is the list of subsets: " + str(find_subsets(['A', 'B', 'C'])))


main()
