#!/usr/bin/env python3
""" LIFOCache module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Class"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            else:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    first_in_item = list(self.cache_data.items())[-1]
                    print("DISCARD: {}".format(first_in_item[0]))
                    del self.cache_data[first_in_item[0]]
                self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
