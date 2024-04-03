class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def is_ll_palindromic(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    second_half_head = reverse_ll(slow.next)
    current1 = head
    current2 = second_half_head
    is_palindrom = True
    while current1 and current2:
        if current1.value != current2.value:
            is_palindrom = False
            break
        current1 = current1.next
        current2 = current2.next

    reverse_ll(second_half_head)
    return is_palindrom
    


def reverse_ll(head):
    prev = None
    current = head
    next = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def create_ll(arr):
    head = Node(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    return head

def ll_to_arr(head):
    arr = []
    current = head
    while current:
        arr.append(current.value)
        current = current.next
    return arr

def main():
    input = (
        [1, 2, 3, 2, 1],
        [1, 2, 3, 3, 2, 1],
        [3, 2, 1],
        [10],
        [1, 2],
    )

    # print(ll_to_arr(create_ll([1, 2, 3, 4, 5])))

    for i in range(len(input)):
        print('---')
        print(str(i + 1) + '. Input: ' + str(input[i]))
        print(str(i + 1) + '. Result ' + str((is_ll_palindromic(create_ll(input[i])))))

main()
