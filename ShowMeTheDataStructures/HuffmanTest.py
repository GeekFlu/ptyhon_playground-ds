import sys
import unittest

from ShowMeTheDataStructures.huffman import huffman_encoding, huffman_decoding


class HuffmanTest(unittest.TestCase):

    def test_encode_huffman(self):
        a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
        print(f"The content of the data is: {a_great_sentence}")
        print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
        print(f"The content of the encoded data is: {encoded_data}")
        self.assertEqual(encoded_data, "1010101010101000100100111111111111111000000010101010101")

    def test_decode_huffman(self):
        data = "AAAAAAABBBCCCCCCCDDEEEEEE"
        encoded_data, tree = huffman_encoding(data)
        decoded_data = huffman_decoding(encoded_data, tree)
        self.assertEqual(data, decoded_data)

        data = "Gyomei is a hulking figure among the Demon Slayers. He is one of the tallest characters in the series, easily towering over his fellow Hashira. He is powerfully built and extremely muscular. He has spiky black hair and a prominent scar running horizontally across his forehead. Having been blind since childhood, he has white eyes with no visible irises or pupils. His eyes frequently tear-up when he gets emotional."
        encoded_data, tree = huffman_encoding(data)
        print(f"The size of the data is: {sys.getsizeof(data)}")
        print(f"The content of the data is: {data}")
        print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
        print(f"The content of the encoded data is: {encoded_data}")
        decoded_data = huffman_decoding(encoded_data, tree)
        self.assertEqual(data, decoded_data)
