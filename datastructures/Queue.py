class Queue:

    def __init__(self, init_capacity=10):
        # to keep reference from head of the queue
        self.head = 0
        # to keep reference from tail of the queue
        self.tail = 0
        self.capacity = init_capacity
        self.arr = [None for _ in range(self.capacity)]
        self.queue_size = 0

    def enqueue(self, value):
        """Adds data to the back of the queue"""
        self.arr[self.tail] = value
        self.tail += 1
        self.queue_size += 1

    def dequeue(self):
        """removes data from the front of the queue"""
        if not self.is_empty():
            value = self.arr[self.head]
            self.arr[self.head] = None
            self.head += 1
            self.queue_size -= 1
            return value
        else:
            return None

    def _handle_full_capacity(self):
        """increases the capacity of the array, for cases in which the queue would otherwise overflow"""
        pass

    def front(self):
        """returns the element at the front of the queue"""
        if self.head is None:
            return -1
        return self.arr[head]

    def size(self):
        """size - returns the number of elements present in the queue"""
        return self.queue_size

    def is_empty(self):
        return self.queue_size <= 0
