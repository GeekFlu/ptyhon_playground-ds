class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


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
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

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

    def duplicate(self):
        return LinkedList(self.to_list())

    def __str__(self):
        cur_head = self.head
        if cur_head is None:
            return "<EMPTY LINKED LIST>"
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def get_unique_element_list(self):
        """This method returns a linked list with unique elements of the original list"""
        if self.head is None:
            return None
        d = dict()
        current = self.head
        while current is not None:
            if d.get(current.value) is None:
                d[current.value] = 1
            else:
                d[current.value] += 1
            current = current.next
        l_simplified = LinkedList()
        for key, value in d.items():
            l_simplified.append(value)
        return l_simplified


def union(llist_1, llist_2):
    """
    Union of two linked list, we are going to use a HashMap to store the occurrences
    :param llist_1: Linked List1
    :param llist_2: Linked list2
    :return: union of 2 linked list
    """
    if llist_1 is None and llist_2 is None:
        return None
    elif llist_1 is None:
        return llist_2.get_unique_element_list()
    elif llist_2 is None:
        return llist_1.get_unique_element_list()

    # we will iterate through the l1 and re link each node to the union list
    union_list = LinkedList()
    map_ = dict()
    update_map_elements(llist_1, map_)
    update_map_elements(llist_2, map_)
    for key, value in map_.items():
        union_list.append(key)

    return union_list


def update_map_elements(linked_list, dictionary):
    current = linked_list.head
    while current is not None:
        if dictionary.get(current.value) is None:
            dictionary[current.value] = 1
        else:
            dictionary[current.value] += 1
        current = current.next


def intersection(llist_1, llist_2):
    """We are going to use a hash map to keep track of the frequency of the elements only frequencies >= 2 will be added to ths final intersection list"""
    if llist_1 is None and llist_2 is None:
        return None
    elif llist_1 is None:
        return llist_2
    elif llist_2 is None:
        return llist_1
    intersection_list = LinkedList()
    map_ = dict()
    if llist_1.size() < llist_2.size():
        update_map_elements(llist_1, map_)
        current = llist_2.head
    else:
        update_map_elements(llist_2, map_)
        current = llist_1.head

    while current is not None:
        if map_.get(current.value) is not None:
            intersection_list.append(current.value)
            map_.pop(current.value)
        current = current.next

    return intersection_list


if __name__ == "__main__":
    # Test case 1
    l1 = LinkedList([3, 6, 9, 9, 1, 20])
    l2 = LinkedList([9, 2, 3, 4, 5])
    print(union(l1, l2))
    print(intersection(l1, l2))
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))
    print(intersection(linked_list_2, linked_list_1))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))
