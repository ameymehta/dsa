class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def find_middle_of_ll(head):
    # if head.next == None:
    #     return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def create_ll(arr):
    head = Node(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next 
    return head

def print_ll(head):
    current = head
    result = []
    while current.next:
        result.append(current.value)
        current = current.next
    print(result)

def main():
    inputs = (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [10],
        [1, 2],
    )
    for i in range(len(inputs)):
        print('---')
        print('Input for case ' + str(i))
        print(inputs[i])
        middle = find_middle_of_ll(create_ll(inputs[i]))
        print(middle.value)

main()
