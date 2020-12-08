from datastructures.LinkedList import Node


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        n = Node(value)
        if self.head is None:
            self.head = n
            self.num_elements += 1
        else:
            n.next = self.head
            self.head = n
            self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.head is not None:
            n = self.head
            self.head = n.next
            self.num_elements -= 1
            return n.value
        else:
            return None
