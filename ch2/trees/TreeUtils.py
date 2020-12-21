from datastructures.Tree import BinaryTree, TreeNode


def get_sample_tree():
    tree = BinaryTree("apple")
    tree.get_root().set_left_child(TreeNode("banana"))
    tree.get_root().set_right_child(TreeNode("cherry"))

    banana_node = tree.get_root().get_left_child()
    banana_node.set_left_child(TreeNode("dates"))
    banana_node.set_right_child(TreeNode("No"))

    dates_node = banana_node.get_left_child()
    dates_node.set_left_child(TreeNode("Another"))

    cherry_node = tree.get_root().get_right_child()
    cherry_node.set_left_child(TreeNode("2"))
    cherry_node.set_right_child(TreeNode("3"))

    two_node = cherry_node.get_left_child()
    two_node.set_left_child(TreeNode("x"))
    two_node.set_right_child(TreeNode("y"))

    three_node = cherry_node.get_right_child()
    three_node.set_right_child(TreeNode("7"))
    return tree
