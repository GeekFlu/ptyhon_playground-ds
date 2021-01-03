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

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def peek(self):
        if self.head is None:
            return None
        n = self.head
        return n

    def pop(self):
        if self.head is not None:
            n = self.head
            self.head = n.next
            self.num_elements -= 1
            return n.value
        else:
            return None

    def _from_linked_list_to_array(self):
        """this method is for learning purposes we are converting the linked list to a list"""
        arr = []
        if self.size() > 0:
            current = self.head
            while current is not None:
                arr.append(current.value)
                current = current.next
            return arr
        else:
            return arr

    def __str__(self):
        if self.size() > 0:
            s = "\n<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self._from_linked_list_to_array()])
            s += "\n_________________\n<bottom of stack>"
            return s
        else:
            return "<stack is empty>"
