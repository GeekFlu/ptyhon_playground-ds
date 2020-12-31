import unittest

from ShowMeTheDataStructures.huffman import HuffmanNode, MinHeap
from utils.test_utils import generate_test_data


class MinHeapTest(unittest.TestCase):

    def test_create_min_heap(self):
        data = [1, 67, 33, -5, 0, 6, 8, -43, -1, 7, 8, 34, 54, 23, 43, -1, 3, -1]
        min_heap = MinHeap()
        for num in data:
            node_ = HuffmanNode('test', num)
            min_heap.insert(node_)

        self.assertIsNotNone(min_heap, "min heap not created correctly")
