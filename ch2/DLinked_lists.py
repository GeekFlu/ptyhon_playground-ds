class DoubleNode:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        if self.head is None:
            self.head = DoubleNode(val)
            self.tail = self.head
        else:
            self.tail.next = DoubleNode(val)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(-2)
    linked_list.append(4)

    print("Going forward through the list, should print 1, -2, 4")
    node = linked_list.head
    while node:
        print(node.value)
        node = node.next

    print("\nGoing backward through the list, should print 4, -2, 1")
    node = linked_list.tail
    while node:
        print(node.value)
        node = node.previous