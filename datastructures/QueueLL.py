from datastructures.LinkedList import Node


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.elements = 0

    def enqueue(self, value):
        """Adds data to the back of the queue"""
        n = Node(value)
        if self.head is None:
            self.head = n
            self.tail = self.head
        else:
            if self.head == self.tail:
                self.head.next = n
                self.tail = n
            else:
                self.tail.next = n
                self.tail = n
        self.elements += 1

    def dequeue(self):
        """removes data from the front of the queue"""
        if self.head is not None:
            val = self.head.value
            self.head = self.head.next
            self.elements -= 1
            return val
        return None

    def _handle_full_capacity(self):
        """increases the capacity of the array, for cases in which the queue would otherwise overflow"""
        pass

    def front(self):
        """returns the element at the front of the queue"""
        if self.head is not None:
            return self.head.value
        return None

    def size(self):
        """size - returns the number of elements present in the queue"""
        return self.elements

    def is_empty(self):
        """
        Checks if Stack is empty
        :return: True if Stack is empty
        """
        return self.elements <= 0
