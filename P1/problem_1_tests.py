import unittest
from utils.test_utils import generate_test_data

from problem_1 import LRUCache, Queue


class LRUTestCase(unittest.TestCase):

    def test_LRU_creation(self):
        cache = LRUCache()
        self.assertIsNotNone(cache)
        self.assertEqual(3, cache.capacity)
        self.assertEqual(0, cache.queue.size())
        cache = LRUCache(1)
        self.assertEqual(1, cache.capacity)
        self.assertEqual(0, cache.queue.size())

    def test_LRU_one_element(self):
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

    def test_LRU_big_capacity(self):
        size_cache = 100000
        cache = LRUCache(5000)
        data = generate_test_data(size_cache + 1)
        for number in range(size_cache):
            cache.set(data[number], data[number])
        last = data[-1]
        cache.set(last, last)
        self.assertEqual(cache.get(last), last)

    def test_invalid_capacity(self):
        with self.assertRaises(Exception) as context:
            LRUCache(-1)

        with self.assertRaises(Exception) as context:
            LRUCache(0)

        with self.assertRaises(Exception) as context:
            LRUCache(None)

    def test_queue_creation(self):
        with self.assertRaises(Exception) as context:
            Queue(0)
        with self.assertRaises(Exception) as context:
            Queue(-1)
        with self.assertRaises(Exception) as context:
            Queue(None)

    def test_queue_enqueue_dequeue_size(self):
        queue_ = Queue(3)
        queue_.enqueue(1)
        queue_.enqueue(2)
        queue_.enqueue(3)
        queue_.enqueue(4)
        queue_.enqueue(5)
        queue_.enqueue(6)
        self.assertEqual(1, queue_.dequeue())
        self.assertEqual(2, queue_.dequeue())
        self.assertEqual(3, queue_.dequeue())
        self.assertEqual(3, queue_.size())

    def test_queue_push(self):
        q = Queue(1)
        q.push(1, 1)
        self.assertEqual(1, q.dequeue())
        self.assertEqual(None, q.dequeue())

        q.push(1, "hola")
        q.push(2, "mundo")
        self.assertEqual(1, q.size())
        self.assertEqual("mundo", q.dequeue())


if __name__ == "__main__":
    unittest.main()
