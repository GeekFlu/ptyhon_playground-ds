import sys
import unittest

from ShowMeTheDataStructures.huffman import huffman_encoding


class HuffmanTest(unittest.TestCase):

    def test_encode_huffman(self):
        a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
        print(f"The content of the data is: {a_great_sentence}")
        print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
        print(f"The content of the encoded data is: {encoded_data}")
        self.assertEqual(encoded_data, "1010101010101000100100111111111111111000000010101010101")