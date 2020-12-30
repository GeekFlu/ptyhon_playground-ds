import sys


def huffman_encoding(data):
    pass


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print(f"The content of the data is: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print(f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
