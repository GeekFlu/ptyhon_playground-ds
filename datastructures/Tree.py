class Node:
    def __init__(self, value):
        self.value = value
        self.left: Node = None
        self.right: Node = None
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


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def get_root(self):
        return self.root
