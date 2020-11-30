def create_linked_list_better(input_list_):
    head_ = None
    tail_ = None
    for value in input_list_:
        if head_ is None:
            head_ = Node(value)
            tail_ = head_
        else:
            tail_.next = Node(value)
            tail_ = tail_.next
    return head_


def print_link_list(head_):
    current_node = head_

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


def create_linked_list(input_list_):
    """
    Function to create a linked list
    @param input_list_: a list of integers
    @return: head node of the linked list
    """
    head_ = None
    for value in input_list_:
        if head_ is None:
            head_ = Node(value)
        else:
            current_n = head_
            while current_n.next is not None:
                current_n = current_n.next
            current_n.next = Node(value)

    return head_


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None



if __name__ == "__main__":
    head = Node(2)
    head.next = Node(1)
    print_link_list(head)

    print("__________________________________________________________________________________")
    input_list = [1, 2, 3, 4, 5, 6]
    head = create_linked_list(input_list)
    print_link_list(head)

    print("__________________________________________________________________________________")
    input_list = [1, 2, 3, 4, 5, 6, 8, 9, 20, 11]
    head = create_linked_list_better(input_list)
    print_link_list(head)
