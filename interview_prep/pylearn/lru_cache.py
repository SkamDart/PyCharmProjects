from collections import deque


class LRUCache(object):
    """
    LeetCode 146. LRU Cache Data Structure

    Contains the following methods
    get and put
    """
    def __init__(self, capacity):
        self._capacity = capacity
        self._cache = {}
        self._lru = deque()
        self._size = 0

    def __str__(self):
        """
        Overrides default __str__ method and returns
        a human readable format for our LRU data structure

        U
        :return:
        """
        return "%s %s" % (self.lru.__str__(), self.cache.__str__())

    @property
    def capacity(self):
        """
        The maximum amount the cache can hold
        :return:
        """
        return self._capacity

    @property
    def cache(self):
        """
        key-value storage representing our cache
        :return:
        """
        return self._cache

    @property
    def lru(self):
        """
        python collections deque representing our "TIMER"
        In our functions, we will always insert into the left
        and evict from the right
        :return:
        """
        return self._lru

    @capacity.setter
    def capacity(self, capacity):
        """
        Set the max value of our cache
        Should only be called in __init__
        :param capacity:
        :return:
        """
        if capacity <= 0:
            raise ValueError('Invalid Capacity')
        else:
            self.capacity = capacity

    @property
    def size(self):
        """
        Get current amount of
        :return:
        """
        return len(self.cache.keys())

    def contains(self, key):
        """
        :param key:
        :return:
        """
        return key in self.cache

    def lru_evict(self):
        """
        Pops from the right of our deque
        :return:
        """
        return self.lru.pop()

    def lru_insert(self, key):
        """
        Inserts into the left of our deque
        :param key:
        :return:
        """
        self.lru.appendleft(key)

    def cache_insert(self, key, value):
        """
        Inserts into our cache
        :param key:
        :param value:
        :return:
        """
        self.cache[key] = value

    def insert(self, key, value):
        """ Inserts k/v pair into cache and LRU queue
        :param key:
        :param value:
        :return:
        """
        self.cache_insert(key, value)
        self.lru_insert(key)

    def cache_remove(self, key):
        """Asserts a key is contained in our cache,
        then removes it.
        :param key:
        :return:
        """
        if self.contains(key):
            del self.cache[key]

    def cache_get(self, key):
        """Wrapper for get from our python dictionary
        :param key:
        :return:
        """
        return self.cache[key]

    def renew(self, key):
        """Our key has been recently used so put it back
        at the front of our queue
        :param key:
        :return:
        """
        self.lru.remove(key)
        self.lru_insert(key)

    def update(self, key, value):
        """Updates a given keys value
        :param key:
        :param value:
        :return:
        """
        self.cache_insert(key, value)

    def get(self, key):
        """Given a key from the user checks if it is valid
        and returns the value associated or -1
        :param key:
        :return:
        """
        if self.contains(key):
            self.renew(key)
            return self.cache_get(key)
        else:
            return -1

    def put(self, key, value):
        """ Inserts k,v pair into our hash
        :param key:
        :param value:
        :return:
        """

        # Update an already contained key
        if self.contains(key):
            self.renew(key)
            self.update(key, value)
            return

        # Evicts Least Recently Used
        elif self.capacity == self.size:
            least_used = self.lru_evict()
            self.cache_remove(least_used)

        # None apply, insert anyway
        self.insert(key, value)
