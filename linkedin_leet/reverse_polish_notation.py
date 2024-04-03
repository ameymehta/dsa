def evalRpn(tokens):
    stack = []
    for token in tokens:
        if token not in '+-/*':
            stack.append(int(token))
            continue

        number_2 = stack.pop()
        number_1 = stack.pop()

        result = 0

        if token == '+':
            result = number_1 + number_2
        elif token == '-':
            result = number_1 - number_2
        elif token == '*':
            result = number_1 * number_2
        else:
            result = number_1 / number_2

        stack.append(result)

    return stack.pop()


def main():
    tokens = ['3', '4', '+']
    print(evalRpn(tokens))

    tokens = ['6', '-132', '/']
    print(evalRpn(tokens))

    tokens = ['1', '2', '+', '3', '4', '-', '+', '5', '6', '*', '7', '8', '/', '+', '+']
    print(evalRpn(tokens))

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRpn(tokens))


main()
