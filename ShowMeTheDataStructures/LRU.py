"""
LRU Implementation
We use two data structures to implement an LRU Cache.

    1. Queue which is implemented using a doubly linked list. The maximum size of the queue will be equal to the total
    number of frames available (cache size). The most recently used pages will be near front end and least recently
    pages will be near the rear end.

    2. A Hash with page number as key and address of the corresponding queue node as value.

When a page is referenced, the required page may be in the memory. If it is in the memory, we need to detach the node
of the list and bring it to the front of the queue.
If the required page is not in memory, we bring that in memory. In simple words, we add a new node to the front
of the queue and update the corresponding node address in the hash. If the queue is full,
i.e. all the frames are full, we remove a node from the rear of the queue,
and add the new node to the front of the queue.
"""


class Node(object):
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

    def get_value(self):
        return self.value


class Queue(object):

    def __init__(self, cache_size=3):
        self.cache_size = cache_size
        self.front = None
        self.tail = None
        self.elements = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.elements += 1

    def dequeue(self):
        """removes data from the front of the queue"""
        if self.front is not None:
            val = self.front.value
            self.front = self.front.next
            self.front.prev = None
            self.elements -= 1
            return val
        return None

    def is_empty(self):
        return self.elements <= 0

    def _from_linked_list_to_array(self, reverse=False):
        arr = []
        if not reverse:
            current: Node = self.front
            while current is not None:
                arr.append(current.get_value())
                current = current.next
        else:
            current: Node = self.tail
            while current is not None:
                arr.append(current.get_value())
                current = current.prev
        return arr

    def size(self):
        return self.elements

    def print(self, reverse=False):
        if not self.is_empty():
            if reverse:
                s = "______________\n<REAR>\n______________\n"
            else:
                s = "______________\n<FRONT>\n______________\n"
            s += "\n______________\n".join([str(item) for item in self._from_linked_list_to_array(reverse)])
            if reverse:
                s += "\n______________\n<FRONT>"
            else:
                s += "\n______________\n<REAR>"

            return s
        else:
            return "<Queue EMPTY>"


class LRUCache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.queue = Queue(capacity)
        self.h_map = dict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        node = self.h_map.get(key)
        if node is not None:
            pass
        return None

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        pass


if __name__ == "__main__":
    reverse_ = True
    d = dict()
    print(f"prueba = {d.get(1)}")
    queue_ = Queue()
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

    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    our_cache.get(1)  # returns 1
    our_cache.get(2)  # returns 2
    our_cache.get(9)  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    our_cache.get(3)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


