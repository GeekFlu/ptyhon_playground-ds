from datastructures.StackLL import Stack
from datastructures.Tree import BinaryTree, Node


def print_data():
    print(f"\n"
          f"        visit_order {visit_order} \n"
          f"        stack:\n"
          f"        {stack}\n"
          f"        ")


if __name__ == "__main__":
    # create a tree and add some nodes
    tree = BinaryTree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))

    visit_order = list()
    stack = Stack()

    # we start by the root node
    stack.push(tree.get_root())
    visit_order.append(tree.get_root().get_value())
    current_node = tree.get_root()

    print_data()

    print(f"{current_node} has left node? {current_node.has_left_child()}")
    if current_node.has_left_child():
        current_node = current_node.get_left_child()
        stack.push(current_node)

    print_data()

    # visit banana
    print(f"visit {current_node}")
    visit_order.append(current_node.get_value())
    print(f"""visit_order {visit_order}""")

    print(f"{current_node} has left node? {current_node.has_left_child()}")
    if current_node.has_left_child():
        current_node = current_node.get_left_child()
        stack.push(current_node)

    print_data()

    # visit banana
    print(f"visit {current_node}")
    visit_order.append(current_node.get_value())
    print(f"""visit_order {visit_order}""")

    print(f"{current_node} has left node? {current_node.has_left_child()}")
    print(f"{current_node} has right node? {current_node.has_right_child()}")

    # since "dates" is a leaf node (has no children), we can start to retrace our steps
    # in other words, we can pop it off the stack.
    print(stack.pop())
    # now we'll set the node to the new top of the stack, which is banana
    current_node = stack.top()
    print(current_node)

    # we already checked for banana's left child, so we'll check for its right child
    print(f"{current_node} has right child? {current_node.has_right_child()}")

    # banana doesn't have a right child, so we're also done tracking it.
    # so we can pop banana off the stack
    print(f"pop {stack.pop()} off stack")
    print_data()
    # now we'll track the new top of the stack, which is apple
    current_node = stack.top()
    print(current_node)

    # we've already checked if apple has a left child; we'll check if it has a right child
    print(f"{current_node} has right child? {current_node.has_right_child()}")

    if current_node.has_right_child():
        current_node = current_node.get_right_child()
        stack.push(current_node)

    print_data()

    # visit cherry
    print(f"visit {current_node}")
    visit_order.append(current_node.get_value())
    print(f"""visit_order: {visit_order}""")
