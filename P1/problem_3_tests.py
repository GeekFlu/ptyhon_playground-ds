import unittest

from problem_3 import MinHeap, HuffmanNode, huffman_encoding, huffman_decoding
from utils.test_utils import generate_test_data


class MinHeapTest(unittest.TestCase):

    def test_create_min_heap(self):
        data = [1, 67, 33, -5, 0, 6, 8, -43, -1, 7, 8, 34, 54, 23, 43, -1, 3, -1]
        min_heap = MinHeap()
        for num in data:
            node_ = HuffmanNode('test', num)
            min_heap.insert(node_)
        self.assertEqual(min_heap.size(), len(data))

        with self.assertRaises(Exception) as context:
            MinHeap(None)

        with self.assertRaises(Exception) as context:
            MinHeap(0)

    def test_encoding_huffman_invalid_data(self):
        encoded_data, tree = huffman_encoding("")
        self.assertEqual(None, encoded_data)
        self.assertEqual(None, tree)

        encoded_data, tree = huffman_encoding(None)
        self.assertEqual(None, encoded_data)
        self.assertEqual(None, tree)

        encoded_data, tree = huffman_encoding("      ")
        self.assertEqual(None, encoded_data)
        self.assertEqual(None, tree)

    def test_encoding_decoding_huffman_valid_data(self):
        data_to_be_encoded = "AAAAAAABBBCCCCCCCDDEEEEEE"
        encoded_data, tree = huffman_encoding(data_to_be_encoded)
        self.assertEqual(encoded_data, "1010101010101000100100111111111111111000000010101010101")
        self.assertIsNotNone(tree)
        self.assertEqual(data_to_be_encoded, huffman_decoding(encoded_data, tree))

        data_to_be_encoded_a = "A"
        data_to_be_encoded_b = "B"
        encoded_data_a, tree_a = huffman_encoding(data_to_be_encoded_a)
        encoded_data_b, tree_b = huffman_encoding(data_to_be_encoded_b)

        # Codification is the same a 0 but the tree have to decode to the correct value
        self.assertEqual(encoded_data_a, encoded_data_b)
        self.assertIsNotNone(tree_b)

        self.assertNotEqual(data_to_be_encoded_b, huffman_decoding(encoded_data_b, tree_a))
        self.assertNotEqual(data_to_be_encoded_a, huffman_decoding(encoded_data_a, tree_b))

        # using the correct tree for the correct value
        self.assertEqual(data_to_be_encoded_a, huffman_decoding(encoded_data_a, tree_a))
        self.assertEqual(data_to_be_encoded_b, huffman_decoding(encoded_data_b, tree_b))


if __name__ == "__main__":
    unittest.main()
