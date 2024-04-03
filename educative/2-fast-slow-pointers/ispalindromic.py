class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return True

    # find middle
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    second_head = reverse(slow)

    # store second head to reverse again at the end
    copy_of_second_head = second_head

    # compare both LL
    while head is not None or second_head is not None:
        if head.value != second_head.value:
            break
        head = head.next
        second_head = second_head.next

    # reset second half
    reverse(copy_of_second_head)

    # if both are none, return true, else return false
    if head is None and second_head is None:
        return True

    return False


def reverse(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
