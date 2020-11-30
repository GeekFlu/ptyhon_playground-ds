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
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

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
        cur = self.head
        while cur.next is not None:
            if cur.value == value:
                return cur
            cur = cur.next

    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            return None
        cur = self.head
        prev = None
        while cur is not None:
            if cur.value == value:
                if prev is not None:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            return None
        n = self.head
        self.head = n.next
        return n.value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """
        cur_pos = 0
        if self.head is None:
            self.append(value)
        else:
            cur = self.head
            prev = None
            nn = Node(value)
            while cur is not None:
                if pos == 0:
                    nn.next = self.head
                    self.head = nn
                    return True
                elif cur_pos == pos:
                    prev.next = nn
                    nn.next = cur
                    return True
                else:
                    prev = cur
                    cur = cur.next
                cur_pos += 1
            # we are in the end of the linked list we insert it
            prev.next = nn
        return True

    def size(self):
        """ Return the size or length of the linked list. """
        size = 0
        if self.head is None:
            return size
        cur = self.head
        while cur is not None:
            size += 1
            cur = cur.next
        return size

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

    def reverse(self):
        """
        Reverse the inputted linked list
        """
        prev = None
        current = self.head
        while current is not None:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.head = prev


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

    # Test search
    linked_list = LinkedList()
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
    assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

    linked_list_remove = LinkedList()
    linked_list_remove.append(1)
    linked_list_remove.append(3)
    linked_list_remove.prepend(2)
    linked_list_remove.prepend(1)
    linked_list_remove.append(4)
    linked_list_remove.append(3)

    # Test remove
    linked_list_remove.remove(1)
    assert linked_list_remove.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list_remove.to_list()}"
    linked_list_remove.remove(3)
    assert linked_list_remove.to_list() == [2, 1, 4, 3], f"list contents: {linked_list_remove.to_list()}"
    linked_list_remove.remove(3)
    assert linked_list_remove.to_list() == [2, 1, 4], f"list contents: {linked_list_remove.to_list()}"

    assert linked_list_remove.size() == 3, f"list contents: {linked_list_remove.to_list()}"

    print(f"value = {linked_list.pop()}")
    print(f"{linked_list.to_list()}")
    print(f"value = {linked_list.pop()}")
    print(f"{linked_list.to_list()}")

    ll = LinkedList()
    ll.prepend(1)
    ll.append(3)
    print(f"Before Insert Linked List = {ll.to_list()}")
    ll.insert(2, 1)
    print(f"After  Insert Linked List = {ll.to_list()}")
    ll.insert(-1, 0)
    print(f"After  Insert Linked List = {ll.to_list()}")
    ll.insert(100, 6)
    print(f"After  Insert Linked List = {ll.to_list()}")
    print(f"Before reverse = {ll.to_list()}")
    ll.reverse()
    print(f"reverse = {ll.to_list()}")
    ll.reverse()
    print(f"reverse = {ll.to_list()}")
