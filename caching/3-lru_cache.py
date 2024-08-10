#!/usr/bin/env python3
""" LRUCache Module """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the LRUCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item in the cache
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the least recently used item (LRU)
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
