from datastructures.LinkedList import Node
from datastructures.Tree import BinaryTree, TreeNode
from datastructures.StackLL import Stack


def preorder_traversal(tree_: BinaryTree):
    if tree_ is None or tree_.root is None:
        return None

    # we set the initial variables and data structures to start the traversal on the tree
    back_track: Stack = Stack()
    order_visit = list()
    current_node: TreeNode = tree_.get_root()
    back_track.push(current_node)
    current_node.set_visited()
    while not back_track.is_empty():
        # Stack is using a a different node implementation so we need to use two get value
        my_node: Node = back_track.peek().get_value()
        my_node.set_visited()
        order_visit.append(my_node.get_value())
        back_track.pop()

        if my_node.has_right_child() and not my_node.get_right_child().is_visited:
            back_track.push(my_node.get_right_child())
        if my_node.has_left_child() and not my_node.get_left_child().is_visited:
            back_track.push(my_node.get_left_child())

    return order_visit


def preorder_traversal_recursive():
    pass


if __name__ == "__main__":
    tree = BinaryTree("apple")
    tree.get_root().set_left_child(TreeNode("banana"))
    tree.get_root().get_left_child().set_left_child(TreeNode("dates"))
    tree.get_root().get_left_child().set_right_child(TreeNode("No"))
    tree.get_root().get_left_child().get_left_child().set_left_child(TreeNode("Another"))

    tree.get_root().set_right_child(TreeNode("cherry"))
    tree.get_root().get_right_child().set_left_child(TreeNode("2"))
    tree.get_root().get_right_child().set_right_child(TreeNode("3"))

    tree.get_root().get_right_child().get_left_child().set_left_child(TreeNode("x"))
    tree.get_root().get_right_child().get_left_child().set_right_child(TreeNode("y"))

    tree.get_root().get_right_child().get_right_child().set_right_child(TreeNode("7"))

    print(preorder_traversal(tree))
