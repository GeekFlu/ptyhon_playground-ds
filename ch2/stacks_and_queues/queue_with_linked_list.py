from datastructures.QueueLL import Queue

if __name__ == "__main__":
    queue_ = Queue()
    queue_.enqueue(1)
    queue_.enqueue(2)
    queue_.enqueue(3)
    queue_.enqueue(4)
    queue_.enqueue(5)
    queue_.enqueue(6)

    print(queue_.dequeue())
    print(queue_.dequeue())
    print(queue_.dequeue())
    print(queue_.dequeue())

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
