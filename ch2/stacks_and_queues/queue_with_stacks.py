# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        self.origin_stack = Stack()
        self.temp_stack = Stack()
        self.elements = 0

    def size(self):
        return self.elements

    def enqueue(self, item):
        self.origin_stack.push(item)
        self.elements += 1

    def dequeue(self):
        if self.origin_stack.size() > 0:
            while self.origin_stack.size() > 0:
                self.temp_stack.push(self.origin_stack.pop())
            val = self.temp_stack.pop()
            while self.temp_stack.size() > 0:
                self.origin_stack.push(self.temp_stack.pop())
            self.elements -= 1
            return val
        return None


if __name__ == "__main__":
    # Setup
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test size
    print("Pass" if (q.size() == 3) else "Fail")

    # Test dequeue
    print("Pass" if (q.dequeue() == 1) else "Fail")

    # Test enqueue
    q.enqueue(4)
    print("Pass" if (q.dequeue() == 2) else "Fail")
    print("Pass" if (q.dequeue() == 3) else "Fail")
    print("Pass" if (q.dequeue() == 4) else "Fail")
    q.enqueue(5)
    print("Pass" if (q.size() == 1) else "Fail")
