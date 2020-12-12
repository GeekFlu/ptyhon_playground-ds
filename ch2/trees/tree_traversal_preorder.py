from datastructures.Tree import BinaryTree, Node
from datastructures.StackLL import Stack


def preorder_traversal(tree_: BinaryTree):
    if tree_ is None or tree_.root is None:
        return None

    # we set the initial variables and data structures to start the traversal on the tree
    back_track: Stack = Stack()
    order_visit = list()
    current_node: Node = tree_.get_root()
    back_track.push(current_node)
    order_visit.append(current_node.get_value())
    current_node.set_visited()
    while current_node is not None:
        if current_node.has_left_child() and not current_node.get_left_child().is_visited:
            current_node = current_node.get_left_child()
            order_visit.append(current_node.get_value())
            current_node.set_visited()
            back_track.push(current_node)
        elif current_node.has_right_child() and not current_node.get_right_child().is_visited:
            # keep track of pattern node
            back_track.push(current_node)

            current_node = current_node.get_right_child()
            order_visit.append(current_node.get_value())
            current_node.set_visited()
            back_track.push(current_node)
        else:
            print(f"Top element = {back_track.top()}")
            if not back_track.is_empty():
                current_node = back_track.pop()
            else:
                current_node = None

    return order_visit


if __name__ == "__main__":
    tree = BinaryTree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))
    tree.get_root().get_left_child().set_right_child(Node("No"))
    tree.get_root().get_left_child().get_left_child().set_left_child(Node("Another"))

    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_right_child().set_left_child(Node("2"))
    tree.get_root().get_right_child().set_right_child(Node("3"))

    tree.get_root().get_right_child().get_left_child().set_left_child(Node("x"))
    tree.get_root().get_right_child().get_left_child().set_right_child(Node("y"))

    tree.get_root().get_right_child().get_right_child().set_right_child(Node("7"))

    print(preorder_traversal(tree))
