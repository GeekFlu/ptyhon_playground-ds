import unittest

from ch3.binary_search import binary_search


class MyTestCase(unittest.TestCase):

    def test_binary_search_iterative(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(5, binary_search(array, 5))
        self.assertEqual(8, binary_search(array, 8))
        self.assertEqual(-1, binary_search(None, 8))
        self.assertEqual(-1, binary_search([], 8))
        self.assertEqual(-1, binary_search([], 88))

    def test_binary_search_recursive(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(8, binary_search(array, 8, False))
        self.assertEqual(5, binary_search(array, 5, False))
        self.assertEqual(-1, binary_search(array, 55, False))
        self.assertEqual(-1, binary_search([], 55, False))




if __name__ == '__main__':
    unittest.main()
