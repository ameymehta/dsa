def get_powerset(arr):
    result = []
    result.append([])
    for element in arr:
        r = len(result)
        for s in range(r):
            subset = list(result[s])
            subset.append(element)
            result.append(subset)
    return result


def is_colorful(nums):
    ps = get_powerset(nums)
    rec = {}
    for i in range(1, len(ps)):
        subset = ps[i]
        prod = 1
        for j in range(len(subset)):
            prod *= subset[j]
        if prod in rec:
            return False
        else:
            rec[prod] = True
    return True


def main():
    t1 = [3, 2, 4, 5]
    print(is_colorful(t1))
    t2 = [3, 2, 6]
    print(is_colorful(t2))


main()
