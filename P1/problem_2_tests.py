import unittest

from problem_2 import find_files


class FileFindingTestCase(unittest.TestCase):

    def test_search_file(self):
        self.assertEqual([], find_files("", ""))
        self.assertEqual([], find_files("", None))
        self.assertEqual([], find_files(None, ""))
        self.assertEqual([], find_files(None, None))
        self.assertEqual([], find_files("", "  "))
        self.assertEqual([], find_files("   ", ""))

        self.assertEqual([], find_files(" invalid ", "./invalid"))
        self.assertEqual([], find_files(".valid", "."))
        self.assertEqual([], find_files(".valid", "./"))

        result = find_files(".c", "./")
        self.assertEqual(4, len(result))

        result = find_files(".gitkeep", "./")
        self.assertEqual(2, len(result))

        result = find_files("_1.py", ".")
        self.assertEqual(1, len(result))


if __name__ == "__main__":
    unittest.main()
