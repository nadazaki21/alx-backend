#!/usr/bin/env python3
""" LFUCache module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.keys_and_uses = {}

    def adjust_uses(self, key):
        """Adjust uses of key"""

        self.keys_and_uses[key] += 1
        # print(self.keys_and_uses)

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.adjust_uses(key)
            else:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    least_used = list(self.keys_and_uses.items())[0][0]
                    # print(f"least used is {least_used}")
                    for k, v in self.keys_and_uses.items():
                        if v < self.keys_and_uses[least_used]:
                            least_used = k
                    print("DISCARD: {}".format(least_used))
                    del self.cache_data[least_used]
                    del self.keys_and_uses[least_used]

                self.cache_data[key] = item
                self.keys_and_uses[key] = 1
                self.adjust_uses(key)

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            self.adjust_uses(key)
            return self.cache_data[key]
        else:
            return None
