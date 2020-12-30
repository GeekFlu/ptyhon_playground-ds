import unittest

from ShowMeTheDataStructures.LRU import LRUCache
from utils.test_utils import generate_test_data


class LRUTestCase(unittest.TestCase):

    def test_LRU_creation(self):
        cache = LRUCache()
        self.assertIsNotNone(cache)
        self.assertEqual(3, cache.capacity)
        self.assertEqual(0, cache.queue.size())
        cache = LRUCache(1)
        self.assertEqual(1, cache.capacity)
        self.assertEqual(0, cache.queue.size())

    def test_LRU_set(self):
        cache = LRUCache(1)
        cache.set(1, 1)
        self.assertEqual(1, cache.get(1))
        self.assertEqual(1, cache.queue.size())
        self.assertEqual(-1, cache.get(34))
        cache.set(3, 1)
        self.assertEqual(1, cache.get(3))
        cache.set(5, 89)
        cache.set(1, 56)
        self.assertEqual(56, cache.get(1))

        size_cache = 100000
        cache = LRUCache(5000)
        data = generate_test_data(size_cache + 1)
        for number in range(size_cache):
            cache.set(data[number], data[number])
        last = data[-1]
        cache.set(last, last)
        assert cache.get(last) == last


if __name__ == "__main__":
    unittest.main()
