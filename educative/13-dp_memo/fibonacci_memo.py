def fibonacci(n):
    memo = {}
    memo[0] = 0
    memo[1] = 1
    memo[2] = 1
    return fibonacci_rec(n, memo)

def fibonacci_rec(n, memo):    
    if n not in memo:
        memo[n] = fibonacci_rec(n-1, memo) + fibonacci_rec(n-2, memo)
    return memo[n]

def main():
    print(fibonacci(200))

main()
