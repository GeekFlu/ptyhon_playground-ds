class Stack:

    def __init__(self, initialize_size=10):
        self.arr = [None for _ in range(initialize_size)]
        self.top = 0
        self.num_elements = 0
        self.capacity = initialize_size

    def pop(self):
        """removes an item from the top of the stack (and returns the value of that item)"""
        val = None
        if self.top > 0:
            val = self.arr[self.top - 1]
            # top - 1 is current top value
            self.arr[self.top - 1] = None
            self.top -= 1
            self.num_elements -= 1
        return val

    def top(self):
        """returns the value of the item at the top of stack (without removing that item)"""
        return self.arr[self.top]

    def push(self, val):
        """adds an item to the top of the stack"""
        if self.num_elements > self.capacity - 1:
            self._handle_stack_capacity_full()
        self.arr[self.top] = val
        self.top += 1
        self.num_elements += 1

    def size(self):
        """returns the size of the stack"""
        return self.num_elements

    def is_empty(self):
        """returns True if the stack is empty and False otherwise"""
        return self.num_elements <= 0

    def print_stack(self):
        """Lets print the stack nicely"""
        pass

    def _handle_stack_capacity_full(self):
        for _ in range(self.capacity):
            self.arr.append(None)
            self.capacity = len(self.arr)
