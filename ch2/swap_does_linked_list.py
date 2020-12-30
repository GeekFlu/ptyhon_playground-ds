from ch2.even_after_odd_nodes import print_linked_list
from ch2.even_after_odd_nodes import create_linked_list

"""
Given a linked list, swap the two nodes present at position i and j, assuming 0 <= i <= j. The positions are based on 0-based indexing.

Note: You have to swap the nodes and not just the values.

Example:

    linked_list = 3 4 5 2 6 1 9
    positions = 2 5
    output = 3 4 1 2 6 5 9

Explanation:
    The node at position 3 has the value 2
    The node at position 4 has the value 6
    Swapping these nodes will result in a final order of nodes of 3 4 5 6 2 1 9

Algorithm:

    PL -> Previous Left Node
    CL -> Current Left Node

    PR -> Previous Right Node
    CR -> Current Right Node

    1) General case, when head node or/and tail node are not swapped

        PL.next = CR
        temp = CR.next
        CR.next = CL.next
        PR.next = CL
        CL.next = temp

    2) If head needs to ber swapped

        2.1 We create a Temporal Head and apply 1) algorithm
            TH -> Temporal Head
    
    3) If elements to be swapped are contiguous 
        PL.next = CR
        temp = CR.next
        if CL == PR
            CR.next = PR
            PR.next = temp
"""


class Node:
    """LinkedListNode class to be used for this problem"""

    def __init__(self, data):
        self.data = data
        self.next = None


def swap_nodes(head, left_index, right_index):
    """
    :param: head- head of input linked list
    :param: `left_index` - indicates position (index) ONE
    :param: `right_index` - indicates position (index) TWO
    return: head of updated linked list with nodes swapped

    Do not create a new linked list
    """
    if head is None:
        return None

    if left_index >= right_index:
        raise ValueError("Left index is grater than Right index")

    previous_left = None
    current_left = None
    previous_right = None
    current_right = None
    temporal_head = Node("Temporal head")
    current = head
    position = 0

    if left_index == 0:
        current_left = head
        previous_left = temporal_head
        temporal_head.next = current_left

    # we go to pl
    while current is not None:
        if position <= left_index - 1:
            previous_left = current
            current_left = current.next

        if position <= right_index - 1:
            previous_right = current
            current_right = current.next
        else:
            break

        current = current.next
        position += 1

    if current_left == head:
        temporal_head.next = current_left

    # Swapping
    previous_left.next = current_right
    temp = current_right.next

    # when elements to be swapped are contiguous
    if current_left == previous_right:
        current_right.next = previous_right
        previous_right.next = temp
    else:
        current_right.next = current_left.next
        previous_right.next = current_left
        current_left.next = temp

    # if we use temporal head
    if left_index == 0:
        head = previous_left.next

    return head


if __name__ == "__main__":
    ll = create_linked_list([3, 4, 5, 2, 6, 1, 9])
    print_linked_list(ll)
    ll_swapped = swap_nodes(ll, 2, 5)
    print_linked_list(ll_swapped)

    arr = [3, 4, 5, 2, 6, 1, 9]
    head_ = create_linked_list(arr)
    print_linked_list(head_)
    head_ = swap_nodes(head_, 3, 4)
    print_linked_list(head_)

    head_ = create_linked_list(arr)
    print_linked_list(head_)
    head_ = swap_nodes(head_, 0, 1)
    print_linked_list(head_)
