import unittest
from LRUCache import LRUCache


class TestLRUCache(unittest.TestCase):

    # Проверяем основной случай, проверяем также что внутри хранятся правильные значения в правильном порядке
    def test_cache_size_2(self):
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
    def test_cache_size_0(self):
        cache = LRUCache(0)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.cache, {})
        self.assertEqual(cache.priority, [])
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), None)

    def test_cache_size_1(self):
        cache = LRUCache(1)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.cache, {"k2": "val2"})
        self.assertEqual(cache.priority, ["k2"])
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), "val2")

    def test_complete_displacement(self):
        cache = LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.cache, {"k1": "val1", "k2": "val2"})
        self.assertEqual(cache.priority, ["k1", "k2"])

        cache.set("k3", "val3")

        self.assertEqual(cache.cache, {"k1": "val1", "k2": "val2", "k3": "val3"})
        self.assertEqual(cache.priority, ["k1", "k2", "k3"])

        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k3"), "val3")

        # Начинаем вытеснение

        cache.set("k4", "val4")
        cache.set("k5", "val5")

        self.assertEqual(cache.cache, {"k3": "val3", "k4": "val4", "k5": "val5"})
        self.assertEqual(cache.priority, ["k3", "k4", "k5"])

        cache.set("k6", "val6")

        self.assertEqual(cache.cache, {"k4": "val4", "k5": "val5", "k6": "val6"})
        self.assertEqual(cache.priority, ["k4", "k5", "k6"])

        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k3"), None)

        self.assertEqual(cache.get("k4"), "val4")
        self.assertEqual(cache.get("k5"), "val5")
        self.assertEqual(cache.get("k6"), "val6")

    def test_new_value_to_existing_key(self):
        cache = LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")

        self.assertEqual(cache.cache, {"k1": "val1", "k2": "val2", "k3": "val3"})
        self.assertEqual(cache.priority, ["k1", "k2", "k3"])

        cache.set("k2", "new_val")

        # Проверим, что в приоритете новое значение теперь в конце(и будет удаляться последним)
        self.assertEqual(cache.cache, {"k1": "val1", "k2": "new_val", "k3": "val3"})
        self.assertEqual(cache.priority, ["k1", "k3", "k2"])

        # Проверим, что новое значение k2 теперь будет удаляться последним через новые set

        cache.set("k4", "val4")
        cache.set("k5", "val5")

        self.assertEqual(cache.cache, {"k4": "val4", "k2": "new_val", "k5": "val5"})
        self.assertEqual(cache.priority, ["k2", "k4", "k5"])

        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), "new_val")
        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k4"), "val4")
        self.assertEqual(cache.get("k5"), "val5")

        self.assertEqual(cache.priority, ["k2", "k4", "k5"])

        cache.set("k6", "val6")

        self.assertEqual(cache.priority, ["k4", "k5", "k6"])
        self.assertEqual(cache.get("k2"), None)


if __name__ == '__main__':
    unittest.main()
