import unittest

from ch3.binary_search import binary_search


class MyTestCase(unittest.TestCase):

    def test_binary_search_iterative(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(5, binary_search(array, 5))
        self.assertEqual(8, binary_search(array, 8))


if __name__ == '__main__':
    unittest.main()
