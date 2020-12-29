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

Reference Links:
- https://www.geeksforgeeks.org/lru-cache-implementation/
"""


class Node(object):
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_val):
        self.value = new_val

    def __repr__(self):
        return f"Node({self.value})"


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

    def insert_node_front(self, node: Node):
        """This method will insert a Node at the front of the Queue"""
        node.next = self.front
        self.front.prev = node
        self.front = node

    def push(self, value):
        """This method will insert a new node at the front, that's why I have selected push as method name"""
        new_node = Node(value)
        val_discarded = None
        if self.front is None:
            self.front = new_node
            self.tail = new_node
        elif self.front == self.tail:
            new_node.next = self.tail
            self.tail.prev = new_node
            self.front = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        if self.size() == self.cache_size:
            val_discarded = self.tail.get_value()
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.elements += 1
        return new_node, val_discarded

    def dequeue(self):
        """removes data from the front of the queue"""
        if self.front is not None:
            val = self.front.value
            self.front = self.front.next
            if self.front is not None:
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
        current: Node = self.h_map.get(key)
        if current is not None:
            prev_: Node = current.prev
            next_: Node = current.next
            # we have to put this node to the front
            if current == self.queue.front:
                # The value is already at the front
                pass
            elif current == self.queue.tail:
                current.prev = None
                prev_.next = None
                self.queue.tail = prev_
                self.queue.insert_node_front(current)
            elif current != self.queue.front:
                prev_.next = current.next
                next_.prev = current.prev
                current.next = None
                current.prev = None
                self.queue.insert_node_front(current)
            return current.get_value()
        return -1

    def set(self, key, value):
        """Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        value does not exist in LRU Cache """
        if self.queue.size() < self.capacity and self.h_map.get(key) is None:
            # we push it to the queue
            node_inserted, value_discarded = self.queue.push(value)
            self.h_map[key] = node_inserted
        else:
            if self.h_map.get(key) is None:
                node_inserted, value_discarded = self.queue.push(value)
                self.h_map[key] = node_inserted
                if value_discarded is not None:
                    self.h_map.pop(value_discarded)
            else:
                node_from_map = self.h_map.get(key)
                node_from_map.set_value(value)


if __name__ == "__main__":
    our_cache = LRUCache(5)

    our_cache.set(1, 1)
    our_cache.set(1, 20)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    assert our_cache.get(1) == 20  # returns 20 #UPDATED value
    assert our_cache.get(2) == 2  # returns 2
    assert our_cache.get(9) == -1  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    print(f"{our_cache.queue.print()}")
    our_cache.set(6, 6)

    assert our_cache.get(3) == -1  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    our_cache.set(3, 33)
    assert our_cache.get(3) == 33  # returns 20 #UPDATED value
    print(f"{our_cache.queue.print()}")
