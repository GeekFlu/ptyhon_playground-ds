import sys


class HuffmanNode(object):

    def __init__(self, letter='', frequency=0):
        self.left: HuffmanNode = None
        self.right: HuffmanNode = None
        self.is_visited = False
        self.letter: str = letter
        self.frequency: int = frequency

    def __repr__(self):
        return f"HuffmanNode(letter={self.letter}, frequency={self.frequency})"

    def __str__(self):
        return f"HuffmanNode(letter={self.letter}, frequency={self.frequency})"


class MinHeap(object):
    """
    MIN Heap class
    """

    def __init__(self):
        self.heap = []

    def size(self):
        if self.heap is None:
            return 0
        return len(self.heap)

    def peek(self):
        """It returns the root element of Min Heap. Time Complexity of this operation is O(1)"""
        if self.heap is None or len(self.heap) <= 0:
            return None
        return self.heap[0]

    def extract_min(self):
        """Always removes the minimum element from Min Heap.
           Time Complexity of this Operation is O(logn) as this operation needs
           to maintain the heap property after removing root."""

    def insert(self, huffman_node: HuffmanNode):
        """
            Inserting a new node takes O(logn) time. We add a new node at the end of the tree.
            IF new node is greater than its parent, then we don’t need to do anything.
            Otherwise, we need to traverse up to fix the violated heap property by swapping.
            using:
            we are going to use an array so:
            to get left child = 2 * index
            to get right child = 2 * index + 1
            to get parent = index / 2 we take the integer part in case of decimal
           """
        if len(self.heap) <= 0:
            self.heap.append(huffman_node)
        else:
            self.heap.append(huffman_node)
            index_inserted = len(self.heap) - 1
            keep_climbing_up = True
            while keep_climbing_up:
                parent_idx = (index_inserted - 1) // 2
                if parent_idx >= 0 and self.heap[index_inserted].frequency < self.heap[parent_idx].frequency:
                    self._swap(index_inserted, parent_idx)
                    index_inserted = parent_idx
                else:
                    keep_climbing_up = False

    def _swap(self, from_idx, with_idx):
        temp = self.heap[from_idx]
        self.heap[from_idx] = self.heap[with_idx]
        self.heap[with_idx] = temp

    def delete(self):
        """Deleting a node also takes O(logn) time."""


class HuffmanTree(object):
    def __init__(self):
        self.root = None

    def set_root(self, root):
        self.root = TreeNode(root)

    def get_root(self):
        return self.root


def huffman_encoding(data):
    pass


def huffman_decoding(data, tree):
    pass


def get_frequency(sentence):
    dictionary = dict()
    if sentence is None or len(sentence) == 0:
        return None
    for character in sentence:
        if dictionary.get(character) is None:
            dictionary[character] = 1
        else:
            dictionary[character] = dictionary.get(character) + 1
    return dictionary


def create_priority_queue(frequency_table: dict):
    """We will create a priority queue using a min heap"""
    if frequency_table is None or len(frequency_table.keys()) <= 0:
        return None
    pr_queue = MinHeap()
    for letter, frequency in frequency_table.items():
        new_node = HuffmanNode(letter, frequency)
        pr_queue.insert(new_node)

    return pr_queue


if __name__ == "__main__":
    # Step 1 determine frequency og each letter
    a_great_sentence = "The bird is the word"

    print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print(f"The content of the data is: {a_great_sentence}")
    codes = get_frequency(a_great_sentence)
    priority_queue = create_priority_queue(codes)
    print("")
    # encoded_data, tree = huffman_encoding(a_great_sentence)
    #
    # print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    # print(f"The content of the encoded data is: {encoded_data}")
    #
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    # print("The content of the encoded data is: {}".format(decoded_data))
