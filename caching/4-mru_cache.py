#!/usr/bin/env python3
""" MRUCache Module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the MRUCache"""
        super().__init__()
        self.cache_data = {}
        self.order = []  # List to track the order of access

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item in the cache
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the most recently used item (MRU)
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add the new item
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end to mark it as recently used (MRU)
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
