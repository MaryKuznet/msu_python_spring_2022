import unittest
from LRUCache import LRUCache


class TestLRUCache(unittest.TestCase):

    # Проверяем основной случай, проверяем также что внутри хранятся правильные значения в правильном порядке
    def test_cache(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.priority, ["k1", "k2"])
        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.priority, ["k2", "k1"])

        cache.set("k3", "val3")

        self.assertEqual(cache.cache, {"k1": "val1", "k3": "val3"})
        self.assertEqual(cache.priority, ["k1", "k3"])
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.priority, ["k1", "k3"])
        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.priority, ["k3", "k1"])

    # Проверяем граничные случаи
    def test_0(self):
        cache = LRUCache(0)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.cache, {})
        self.assertEqual(cache.priority, [])
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), None)

    def test_1(self):
        cache = LRUCache(1)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.cache, {"k2": "val2"})
        self.assertEqual(cache.priority, ["k2"])
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), "val2")


if __name__ == '__main__':
    unittest.main()
