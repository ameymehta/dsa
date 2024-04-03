def fib(n):
    memo = {}
    return fibonacci(n, memo)


def fibonacci(n, memo):
    if(n < 3):
        return 1

    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)

    return memo[n]

def fibonacci_by_loop(n):
    result = []
    result.append(1)
    result.append(1)
    for i in range(1, n-1):
        next = result[i] + result[i-1]
        result.append(next)
    return result
    
def fibonacci_by_recursion(n):
    return fbr(n)

def fbr(n):
    if n < 3:
        return 1
    return fbr(n-1) + fbr(n-2)

def main():
    print(fib(8))
    print(fibonacci_by_loop(8))
    print(fibonacci_by_recursion(8))

main()
