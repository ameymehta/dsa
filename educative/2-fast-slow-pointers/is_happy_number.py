def is_happy_number(num):
    slow = num
    fast = get_sum_of_squares(num)
    while slow != fast:
        slow = get_sum_of_squares(slow)
        fast = get_sum_of_squares(get_sum_of_squares(fast))
    if fast == 1:
        return True
    return False

def get_sum_of_squares(num):
    sum = 0
    while num:
        digit = num % 10
        num = num // 10
        sum += digit ** 2
    return sum

# driver
def main():
    inputs = [1, 5, 19, 25, 7]
    for i in range(len(inputs)):
        print('-----')
        print('Input for case ' + str(i))
        print(inputs[i])
        print('Output for case ' + str(i))
        print(is_happy_number(inputs[i]))

main()
