def find_subsets(elements):
  result = []
  result.append([])
  for e in elements:
    n = len(result)
    for i in range(n):
      s = list(result[i])
      s.append(e)
      result.append(s)
  return result


def main():

    print("Here is the list of subsets: " + str(find_subsets(['A', 'B'])))
    print("Here is the list of subsets: " + str(find_subsets(['A', 'B', 'C'])))


main()
