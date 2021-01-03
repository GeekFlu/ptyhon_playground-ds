import unittest

from problem_6 import LinkedList, union, intersection


class UnionIntersectionLLTests(unittest.TestCase):

    def test_union(self):
        l1 = LinkedList([0, 4, -3, -12, 11])
        l2 = LinkedList([])
        union_ll = union(l1, l2)
        union_lst = union_ll.to_list()
        union_lst_sorted = sorted(union_lst)
        self.assertEqual(union_lst_sorted, [-12, -3, 0, 4, 11])

        l1 = LinkedList([0, 4, -3, -12, 11])
        l2 = None
        union_ll = union(l1, l2)
        union_lst = union_ll.to_list()
        union_lst_sorted = sorted(union_lst)
        self.assertEqual(union_lst_sorted, [-12, -3, 0, 4, 11])

        l1 = LinkedList([])
        l2 = LinkedList([1, -1, 45, 34])
        union_ll = union(l1, l2)
        union_lst = union_ll.to_list()
        union_lst_sorted = sorted(union_lst)
        self.assertEqual(union_lst_sorted, [-1, 1, 34, 45])

        l1 = None
        l2 = LinkedList([1, -1, 45, 34])
        union_ll = union(l1, l2)
        union_lst = union_ll.to_list()
        union_lst_sorted = sorted(union_lst)
        self.assertEqual(union_lst_sorted, [-1, 1, 34, 45])

        l1 = LinkedList([])
        l2 = LinkedList([])
        union_ll = union(l1, l2)
        self.assertIsNone(union_ll)

        union_ll = union(None, None)
        self.assertIsNone(union_ll)

        l1 = LinkedList([1])
        l2 = LinkedList([1])
        union_ll = union(l1, l2)
        union_lst = union_ll.to_list()
        union_lst_sorted = sorted(union_lst)
        self.assertEqual(union_lst_sorted, [1])

        l1 = LinkedList([3, 6, 9, 9, 1, 20])
        l2 = LinkedList([9, 2, 3, 4, 5])
        union_ll = union(l1, l2)
        # we need to convert the linked to a simple list/ array, sort it to verify the union
        union_lst = union_ll.to_list()
        union_lst_sorted = sorted(union_lst)
        self.assertEqual(union_lst_sorted, [1, 2, 3, 4, 5, 6, 9, 20])

    def test_intersection(self):
        linked_list_1 = LinkedList([])
        linked_list_2 = LinkedList([6, 32, 4, 9, 6, 1, 11, 21, 1])
        inter = intersection(linked_list_1, linked_list_2)
        self.assertEqual(inter, None)

        linked_list_1 = LinkedList([6, 32, 4, 9, 6, 1, 11, 21, 1])
        linked_list_2 = LinkedList([])
        inter = intersection(linked_list_1, linked_list_2)
        self.assertEqual(inter, None)

        linked_list_1 = LinkedList([])
        linked_list_2 = LinkedList([])
        inter = intersection(linked_list_1, linked_list_2)
        self.assertEqual(inter, None)

        linked_list_1 = None
        linked_list_2 = LinkedList([])
        inter = intersection(linked_list_1, linked_list_2)
        self.assertEqual(inter, None)

        linked_list_1 = LinkedList([])
        linked_list_2 = None
        inter = intersection(linked_list_1, linked_list_2)
        self.assertEqual(inter, None)

        inter = intersection(None, None)
        self.assertEqual(inter, None)

        linked_list_1 = LinkedList([3, 2, 4, 35, 6, 65, 6, 4, 3, 21])
        linked_list_2 = LinkedList([6, 32, 4, 9, 6, 1, 11, 21, 1])
        inter = intersection(linked_list_1, linked_list_2)
        # we need to convert the linked to a simple list/ array, sort it to verify the intersection
        inter_sorted = sorted(inter.to_list())
        self.assertEqual(inter_sorted, [4, 6, 21])

        # Test case 2

        linked_list_3 = LinkedList([1])
        linked_list_4 = LinkedList([1])

        inter = intersection(linked_list_3, linked_list_4)
        self.assertEqual(inter.to_list(), [1])


if __name__ == "__main__":
    unittest.main()
