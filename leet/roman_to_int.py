def romanToInt(s):
    r_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = []
    for i in s:
        values.append(r_map[i])
    result = 0
    v = 0
    while v < len(values):
        if(v < len(values)-1 and values[v] < values[v+1]):
            result += (values[v+1] - values[v])
            v += 2
        else:
            result += values[v]
            v += 1
    return result


def main():
    print(romanToInt('III'))


main()
