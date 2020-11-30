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


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node_ = self.head
        while node_.next:
            node_ = node_.next

        node_.next = Node(value)
        return

    def to_list(self):
        lst = list()
        cur = self.head
        while cur is not None:
            lst.append(cur.value)
            cur = cur.next
        return lst

    # Define a function outside of the class
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        n = Node(value)
        if self.head is None:
            self.head = n
            return

        n.next = self.head
        self.head = n

    def print_link_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None


if __name__ == "__main__":
    print("__________________________________________________________________________________")
    ll = LinkedList()
    ll.prepend(-1)
    ll.print_link_list()
    print(f"{ll.to_list()}")

    # Test append - 2
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"
