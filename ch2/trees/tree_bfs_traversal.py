from ch2.trees.TreeUtils import get_sample_tree
from datastructures.QueueLL import Queue
from datastructures.Tree import BinaryTree


def bfs(tree_: BinaryTree):
    if tree_ is None:
        return list()
    traversal_list = list()
    queue_keeper = Queue()
    queue_keeper.enqueue(tree_.get_root())
    while not queue_keeper.is_empty():
        node = queue_keeper.dequeue()
        traversal_list.append(node.get_value())
        if node.has_left_child():
            queue_keeper.enqueue(node.get_left_child())
        if node.has_right_child():
            queue_keeper.enqueue(node.get_right_child())
    return traversal_list


if __name__ == "__main__":
    tree = get_sample_tree()
    print(bfs(tree))
