class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def reverse_k_nodes_in_ll(head, k):
    #dummy is the node that points to head
    dummy = Node(0)
    dummy.next = head
    ptr = dummy
    while(ptr != None):
        # tracker is to track if we have k nodes for next segment
        tracker = ptr
        for i in range(k):
            if tracker == None:
                break
            tracker = tracker.next
        if tracker == None:
            break
        previous, current = reverse_ll(ptr.next, k)
        # # previous is going to be head node of newly reversed sub list
        # print(previous.value)
        # # current is the next of last node
        # print(current.value)
        # # ptr is node before the segment sent to reverse. At start it is dummy node
        # print(ptr.value)
        # # ptr.next will point to unreversed ll head (now the last node of reversed ll)
        # # now it needs to be pointing to reversed ll head i.e. previous
        # print(ptr.next.value)
        # print('---')
        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = current
        ptr.next = previous
        ptr = last_node_of_reversed_group
    return dummy.next

def reverse_ll(head, k):
    previous, current, next = None, head, None
    for _ in range(k):
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous, current

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
    input = [[1, 2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 2, 8, 7, 7], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7], [1]]
    k = [3, 2, 1, 7, 1]

    # print(ll_to_arr(create_ll([1, 2, 3, 4, 5])))
    head = create_ll([1, 2, 3, 4, 5, 6, 7, 8])
    print(str(ll_to_arr(reverse_k_nodes_in_ll(head, 3))))

    # for i in range(len(input)):
    #     print('---')
    #     print(str(i + 1) + '. Input: ' + str(input[i]) + '. k = ' + str(k[i]))
    #     head = create_ll(input[i])
    #     print(str(i + 1) + '. Result ' + str(ll_to_arr(reverse_k_nodes_in_ll(head, k[i]))))

main()
