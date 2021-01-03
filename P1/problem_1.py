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
    """
    This is the base class node for the doubly linked list
    """

    def __init__(self, value, key=None):
        self.next = None
        self.prev = None
        self.value = value
        self.key = key

    def get_value(self):
        """Get the value that holds the Node"""
        return self.value

    def set_value(self, new_val):
        """If necessary overrides / updates the value of the current Node instance"""
        self.value = new_val

    def get_key(self):
        return self.key

    def __repr__(self):
        return f"Node({self.value})"


class Queue(object):
    """
    This is a QUEUE implemented with a doubly linked list, we have a window size which will keep only those elements in the Queue
     we have 2 methods to insert into the queue:
        - enqueue inserts a value wrapped into a node @ the rear of the queue
        - push inserts a value wrapped into a node @ the front of the queue
    we have a
        - dequeue method which removes the element @ the front of the queue
        - size method which returns the element count
        - is_empty which returns True if the queue does not have any element
    """

    def __init__(self, window_size=3):
        """
        Creates a Queue with a size for keeping track on only those elements
        :param window_size:
        """
        if window_size is None or window_size <=0:
            raise ValueError("Queue window / capacity should be > 0")
        self.window_size = window_size
        self.front = None
        self.tail = None
        self.elements = 0

    def enqueue(self, value):
        """Enqueues a value wrapped by Node class @ the rear of the Queue"""
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
        """This method will insert a NODE not a value at the front of the Queue"""
        node.next = self.front
        self.front.prev = node
        self.front = node

    def push(self, key, value):
        """This method will insert a new node at the front, if the value is out of the window's queue this Node will be discarded and returned"""
        new_node = Node(value, key)
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

        if self.size() == self.window_size:
            val_discarded = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.elements += 1
        # if there is a value discarded we return it
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

    def __init__(self, capacity=3):
        # Initialize class variables
        if capacity is None or capacity <= 0:
            raise ValueError("Capacity must be grater than 0")
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
            node_inserted, value_discarded = self.queue.push(key, value)
            self.h_map[key] = node_inserted
        else:
            if self.h_map.get(key) is None:
                node_inserted, value_discarded = self.queue.push(key, value)
                self.h_map[key] = node_inserted
                if value_discarded is not None:
                    self.h_map.pop(value_discarded.get_key())
            else:
                node_from_map = self.h_map.get(key)
                node_from_map.set_value(value)
