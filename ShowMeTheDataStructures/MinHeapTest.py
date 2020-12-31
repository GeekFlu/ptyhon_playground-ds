import unittest

from ShowMeTheDataStructures.huffman import HuffmanNode, MinHeap
from utils.test_utils import generate_test_data


class MinHeapTest(unittest.TestCase):

    def create_min_heap(self):
        data = generate_test_data(100)
        min_heap = MinHeap()
        for num in data:
            node_ = HuffmanNode(num)
            min_heap.insert(node_)

        self.assertIsNotNone(min_heap, "min heap not created correctly")
