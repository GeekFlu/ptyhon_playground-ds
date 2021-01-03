from utils.test_utils import generate_test_data
"""
Problem Statement

Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed
after odd numbers. Do not create any new nodes and avoid using any other data structure. The relative order of even
and odd elements must not change.

Example:
    linked list = 1 2 3 4 5 6
    output = 1 3 5 2 4 6
"""


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    if head is None:
        return None

    current = head
    prev = head
    odd_linked_list = Node("Odds")
    current_odd = odd_linked_list

    even_linked_list = Node("Evens")
    current_even = even_linked_list
    while current is not None:
        if current.data % 2 == 0:
            current_even.next = current
            current_even = current_even.next
        else:
            current_odd.next = current
            current_odd = current_odd.next

        current = current.next

    print_linked_list(odd_linked_list)
    print_linked_list(even_linked_list)

    end_of_odds = odd_linked_list
    while end_of_odds.next is not None:
        if end_of_odds.next.data % 2 == 0:
            end_of_odds.next = None
            break
        end_of_odds = end_of_odds.next

    end_of_odds.next = even_linked_list.next
    return odd_linked_list.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    ll = create_linked_list([1, 2, 3, 4, 5, 6])
    print_linked_list(ll)
    print_linked_list(even_after_odd(ll))

    arr = generate_test_data(10)
    print(f"arr = {arr} ")
    ll = create_linked_list(arr)
    print_linked_list(even_after_odd(ll))
