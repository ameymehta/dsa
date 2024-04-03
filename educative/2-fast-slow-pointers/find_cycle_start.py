class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        alist = []
        while temp is not None:
            alist.append(temp.value)
            temp = temp.next
        print(alist)


def find_cycle_start(head):
    slow = head
    fast = head
    cycle_length = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        #print('slow = ' + str(slow.value))
        if(slow == fast):
            #print('slow and fast = ' + str(slow.value))
            cycle_length = count_cycle_length(slow)
            break
    return find_start(head, cycle_length)


def count_cycle_length(slow):
    current = slow.next
    cycle_length = 1
    while current != slow:
        current = current.next
        cycle_length += 1
    #print('Cycle length: ' + str(cycle_length))
    return cycle_length


def find_start(head, cycle_length):
    pointer1 = head
    pointer2 = head
    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
