def staircase(steps):
  memo = {}
  memo[0] = 1
  memo[1] = 1
  memo[2] = 2
  return staircase_rec(steps, memo)

def staircase_rec(steps, memo):  
  if steps not in memo:
    memo[steps] = staircase_rec(steps -1, memo) + staircase_rec(steps -2, memo) + staircase_rec(steps -3, memo)
  return memo[steps]

def main():
  print staircase(3)
  print staircase(4)
  print staircase(5)

main()