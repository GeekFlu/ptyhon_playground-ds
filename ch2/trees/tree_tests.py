from datastructures.Tree import Node

if __name__ == '__main__':
    node0 = Node("apple")
    node1 = Node("banana")
    node2 = Node("orange")
    node0.set_left_child(node1)
    node0.set_right_child(node2)

    print(f"""
    node 0: {node0.value}
    node 0 left child: {node0.left.value}
    node 0 right child: {node0.right.value}
    """)

    node0 = Node("apple")
    node1 = Node("banana")
    node2 = Node("orange")
    print(f"has left child? {node0.has_left_child()}")
    print(f"has right child? {node0.has_right_child()}")

    print("adding left and right children")
    node0.set_left_child(node1)
    node0.set_right_child(node2)

    print(f"has left child? {node0.has_left_child()}")
    print(f"has right child? {node0.has_right_child()}")
