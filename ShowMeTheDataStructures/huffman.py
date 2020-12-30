import sys


class TreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left: TreeNode = None
        self.right: TreeNode = None
        self.is_visited = False

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def set_visited(self):
        self.is_visited = True

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


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


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print(f"The content of the data is: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print(f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))
