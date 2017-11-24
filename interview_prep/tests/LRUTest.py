from unittest import TestCase
from pylearn.lru_cache import LRUCache


class TestLRUCache(TestCase):

    def test_lru_simple(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)

        self.assertTrue(cache.contains(1))
        self.assertTrue(cache.contains(2))
        self.assertTrue(cache.get(1) == 1)

        cache.put(3, 3)

        self.assertTrue(cache.get(2) == -1)

        cache.put(4, 4)

        self.assertTrue(cache.get(1) == -1)
        self.assertTrue(cache.get(3) == 3)
        self.assertTrue(cache.get(4) == 4)

    def test_lru_insert(self):
        cache = LRUCache(2)
        self.assertTrue(-1 == cache.get(2))

        cache.put(2, 6)

        self.assertTrue(-1 == cache.get(1))

        cache.put(1, 5)
        cache.put(1, 2)

        self.assertTrue(2 == cache.get(1))
        self.assertTrue(6 == cache.get(2))

    def test_lru_medium(self):
        cache = LRUCache(2)
        cache.put(2, 1)
        cache.put(1, 1)
        cache.put(2, 3)
        cache.put(4, 1)
        self.assertTrue(-1 == cache.get(1))
        self.assertTrue(3 == cache.get(2))

