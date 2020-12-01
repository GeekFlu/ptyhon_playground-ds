import time
from ch2.generate_numbers import generate_test_data


def merge(list1, list2):
    """
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    """
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    temp = Node('temp')
    cur = temp
    l1 = list1.head
    l2 = list2.head
    while l1 is not None and l2 is not None:
        if l1.value <= l2.value:
            cur.next = l1
            cur = l1
            l1 = l1.next
        else:
            cur.next = l2
            cur = l2
            l2 = l2.next

    if l1 is None:
        cur.next = l2
    if l2 is None:
        cur.next = l1

    return temp.next

def merge_keep_original_lists(list1, list2):
    """
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    """
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    temp = LinkedList()
    temp.append('temp')
    l1 = list1.head
    l2 = list2.head
    while l1 is not None and l2 is not None:
        if l1.value <= l2.value:
            temp.append(l1.value)
            l1 = l1.next
        else:
            temp.append(l2.value)
            l2 = l2.next

    if l1 is None:
        while l2 is not None:
            temp.append(l2.value)
            l2 = l2.next
    if l2 is None:
        while l1 is not None:
            temp.append(l1.value)
            l1 = l1.next

    temp.head = temp.head.next

    return temp

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


def is_circular(l_list):
    if l_list.head is None:
        return False

    slow = l_list.head
    fast = l_list.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # we found a cycle
            return True
    return False


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

    print("__________________________________________________________________________________")
    list_with_loop = LinkedList([2, -1, 3, 0, 5])
    print(f"list_with_loop = {list_with_loop.to_list()}")
    # Creating a loop where the last node points back to the second node
    loop_start = list_with_loop.head.next

    node = list_with_loop.head
    # reach the end node an assign next to the second node of the list
    while node.next:
        node = node.next
    node.next = loop_start

    print(is_circular(list_with_loop))

    # Test Cases

    # Create another circular linked list
    small_loop = LinkedList([0])
    small_loop.head.next = small_loop.head

    print("Pass" if is_circular(list_with_loop) else "Fail")  # Pass
    print("Pass" if is_circular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")  # Fail
    print("Pass" if is_circular(LinkedList([1])) else "Fail")  # Fail
    print("Pass" if is_circular(small_loop) else "Fail")  # Pass
    print("Pass" if is_circular(LinkedList([])) else "Fail")  # Fail

    start = time.time()
    list1 = LinkedList([1, 3, 4])
    list2 = LinkedList([2, 5, 6, 7])
    ll_merged = merge_keep_original_lists(list1, list2)
    print(f"{ll_merged.to_list()}")
    ll_merged = merge_keep_original_lists(LinkedList([-1, 6, 7]), LinkedList([1, 2, 3, 4]))
    print(f"{ll_merged.to_list()}")
    ll_merged = merge_keep_original_lists(None, LinkedList([1, 2, 3, 4]))
    print(f"{ll_merged.to_list()}")
    ll_merged = merge_keep_original_lists(LinkedList([-1, 6, 7]), None)
    print(f"{ll_merged.to_list()}")
    print(f"execution time = {time.time() - start}")

    # long_ll1 = LinkedList(generate_test_data(1000))
    # long_ll2 = LinkedList(generate_test_data(2670))
    # start = time.time()
    # merged_l = merge_keep_original_lists(long_ll1, long_ll2)
    # print(f"Merging big lists execution time = {time.time() - start}")
    # print(f"ehst {merged_l.to_list()[:100]}")

    long_ll1 = LinkedList(generate_test_data(200000))
    long_ll2 = LinkedList(generate_test_data(267000))
    start = time.time()
    merged_node = merge(long_ll1, long_ll2)
    n_merged = LinkedList()
    n_merged.head = merged_node
    print(f"Merging big lists execution time = {time.time() - start}")
    print(f"ehst {n_merged.pop()}")
