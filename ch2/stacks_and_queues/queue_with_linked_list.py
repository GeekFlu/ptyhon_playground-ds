from datastructures.QueueLL import Queue


def reverse_queue(queue: Queue):
    """
    Reverese the input queue

    Args:
       queue(queue),str2(string): Queue to be reversed
    Returns:
       queue: Reversed queue
    """
    prev = None
    current = queue.head
    next_ = queue.head.next
    while current is not None:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_

    temp = queue.head  # this is the new tail
    queue.head = queue.tail
    queue.tail = temp


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

    org_q = Queue()
    org_q.enqueue('L')
    org_q.enqueue('u')
    org_q.enqueue('i')
    org_q.enqueue('s')
    org_q.enqueue('a')
    reverse_queue(org_q)
    print(org_q.dequeue())
    print(org_q.dequeue())
    print(org_q.dequeue())
    print(org_q.dequeue())
    print(org_q.dequeue())
