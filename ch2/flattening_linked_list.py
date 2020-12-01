# Helper code

def merge(list1, list2):
    """
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    """
    temp = Node(-99)
    cur = temp
    l1 = list1.head
    l2 = list2.head
    while l1 is not None and l2 is not None:
        if l1.value <= l2.value:
            cur.next = l1
            cur = l1
            l1 = l1.next
        else:
            cur.next = l2
            cur = l2
            l2 = l2.next


# A class behaves like a data-type, just like an int, float or any other built-in ones.
# User defined class
class Node:
    def __init__(self,
                 value):  # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


# User defined class
class LinkedList:
    def __init__(self, head):  # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''

    def append(self, value):

        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

    '''We will need this function to convert a LinkedList object into a Python list of integers'''

    def to_list(self):
        out = []  # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:  # <-- Iterate untill we have nodes available
            out.append(int(str(
                node.value)))  # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next

        return out
