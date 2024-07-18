#!/usr/bin/python3

""" Basic """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic """

    def put(self, key, item):
        """Puts in cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets from cache"""
        return self.cache_data.get(key, None)
