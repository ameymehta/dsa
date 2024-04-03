class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_nth_node_from_the_end(list, n):
    if len(list) < n:
        return []
    head = create_linked_list(list)
    left = head
    right = head
    for i in range(n):
        right = right.next

    if not right:
        return head.next
    
    while (right.next):
        left = left.next
        right = right.next

    left.next = left.next.next
    return head

def create_linked_list(list):
    head = Node(list[0])
    prev_node = head
    for i in range(1, len(list)):
        node = Node(list[i])
        prev_node.next = node
        prev_node = node
    return head

def print_linked_list(head):
    current = head
    result = []
    while current.next != None:
        result.append(current.value)
        current = current.next
    result.append(current.value)
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
        output_head = remove_nth_node_from_the_end(input_list, input_n)
        print('Output case ' + str(i+1))
        print_linked_list(output_head)

main()