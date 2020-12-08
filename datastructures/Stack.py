class Stack:

    def __init__(self, initialize_size=10):
        self.arr = [None for _ in range(initialize_size)]
        self.top = 0
        self.size = 0

    def pop(self):
        """removes an item from the top of the stack (and returns the value of that item)"""
        pass

    def top(self):
        """returns the value of the item at the top of stack (without removing that item)"""
        pass

    def push(self, val):
        """adds an item to the top of the stack"""
        pass

    def size(self):
        """returns the size of the stack"""
        return self.size

    def is_empty(self):
        """returns True if the stack is empty and False otherwise"""
        return self.size <= 0
