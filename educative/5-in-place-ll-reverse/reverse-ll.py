class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def reverse_ll(head):
    prev = None
    current = head
    next = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head

def create_ll(arr):
    head = Node(arr[0])
    current = head
    for i in range (1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    return head

def ll_to_arr(head):
    result = []
    current = head
    while current.next:
        result.append(current.value)
        current = current.next
    result.append(current.value)
    return result

def main():
    input = (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [10],
        [1, 2],
    )

    # print(ll_to_arr(create_ll([1, 2, 3, 4, 5])))

    for i in range(len(input)):
        print('---')
        print(str(i + 1) + '. Input: ' + str(input[i]))
        print(str(i + 1) + '. Result ' + str(ll_to_arr(reverse_ll(create_ll(input[i])))))

main()
