class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def remove_nth_from_last(arr, n):
    head = create_ll(arr)
    right = head
    left = head
    for i in range(n):
        right = right.next

    if not right:
        return head
    
    while right.next:
        left = left.next
        right = right.next
    
    left.next = left.next.next

    return head


def create_ll(arr):
    head = Node(arr[0])
    current = head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        current.next = new_node
        current = current.next
    return head

def print_ll(head):
    current = head
    result = []
    while current:
        result.append(current.value)
        current = current.next
    print(result)

#Driver
def main():
    lists = [[23, 89, 10, 5, 67, 39, 70, 28], [34, 53, 6, 95, 38, 28, 17, 63, 16, 76], [288, 224, 275, 390, 4, 383, 330, 60, 193],
    [1, 2, 3, 4, 5, 6, 7, 8, 9], [69, 8, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12]]
    n = [4, 1, 6, 9, 11]

    for i in range(len(n)):
        print('------')
        print('Input case ' + str(i+1))
        input_list = lists[i]
        print(input_list)
        input_n = n[i]
        print(input_n)
        output_head = remove_nth_from_last(input_list, input_n)
        print('Output case ' + str(i+1))
        print_ll(output_head)

main()