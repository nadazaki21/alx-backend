#!/usr/bin/env python3
""" BasicCache module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
