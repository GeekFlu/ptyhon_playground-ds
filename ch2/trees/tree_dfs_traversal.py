from ch2.trees.TreeUtils import get_sample_tree
from datastructures.LinkedList import Node
from datastructures.QueueLL import Queue
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


def preorder_traversal_recursive(tree_: BinaryTree):
    if tree_ is None or tree_.root is None:
        return None

    order_traversal = list()
    preorder(tree_.get_root(), order_traversal)
    return order_traversal


def preorder(node_: TreeNode, order_list: list):
    if node_ is None:
        return
    order_list.append(node_.get_value())
    preorder(node_.get_left_child(), order_list)
    preorder(node_.get_right_child(), order_list)


def inorder(node_: TreeNode, order_list: list):
    if node_ is None:
        return
    preorder(node_.get_left_child(), order_list)
    order_list.append(node_.get_value())
    preorder(node_.get_right_child(), order_list)


def preorder(node_: TreeNode, order_list: list):
    if node_ is None:
        return
    preorder(node_.get_left_child(), order_list)
    preorder(node_.get_right_child(), order_list)
    order_list.append(node_.get_value())


if __name__ == "__main__":
    tree = get_sample_tree()
    assert preorder_traversal(tree) == ['apple', 'banana', 'dates', 'Another', 'No', 'cherry', '2', 'x', 'y', '3', '7']
    tree = get_sample_tree()
    tracersal_recursiver = preorder_traversal_recursive(tree)
    assert tracersal_recursiver == ['apple', 'banana', 'dates', 'Another', 'No', 'cherry', '2', 'x', 'y', '3', '7']
