#!/usr/bin/python3
""" FIFO caching: Create new class FIFOCache that inherits BaseCaching
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO Cache.
    Inherits all behaviors from BaseCaching. Any attempt to
    add an entry to the cache when it is at max capacity (as specified by
    BaseCaching.MAX_ITEMS), it discards the oldest entry to accommodate for
    the new one.
    Attributes:
      __init__ - method that initializes class instance
      put - method that adds key-value pair to cache
      get - method that retrieves key-value pair from cache"""

    def __init__(self):
        """Initialize class instances"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add key-value pair to cache system
        If cache is  max capacity,
        discard oldest entry in cache to accommodate new entry"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {:s}".format(discard))

    def get(self, key):
        """Return value stored in `key` key of cache.
        If key is None or does not exist in cache, return None."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
    
    