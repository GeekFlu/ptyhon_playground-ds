from ShowMeTheDataStructures.LRU import Queue

if __name__ == "__main__":
    reverse_ = True
    d = dict()
    print(f"prueba = {d.get(1)}")
    queue_ = Queue(3)
    print(f"{queue_.print()}")
    queue_.enqueue(1)
    queue_.enqueue(2)
    queue_.enqueue(3)
    queue_.enqueue(4)
    queue_.enqueue(5)
    queue_.enqueue(6)
    print(f"size = {queue_.size()}")
    print(f"{queue_.print()}")
    print(f"{queue_.print(reverse_)}")
    print(f"value = {queue_.dequeue()}")
    print(f"value = {queue_.dequeue()}")
    print(f"value = {queue_.dequeue()}")
    print(f"{queue_.print()}")
    print(f"{queue_.print(reverse_)}")
    print(f"size of queue = {queue_.size()}")
    queue_.dequeue()
    queue_.dequeue()
    queue_.push(3)
    queue_.dequeue()
    queue_.dequeue()
    print(f"{queue_.print()}")

    queue_.push(4)
    queue_.push(5)
    queue_.push(6)
    print(f"{queue_.print()}")
    print(f"{queue_.print(True)}")
    queue_.push(7)
    print(f"{queue_.print()}")