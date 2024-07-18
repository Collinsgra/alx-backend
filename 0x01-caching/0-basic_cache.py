#!/usr/bin/env python3
""" BaseCaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Create a class BasicCache
    """
    def __init__(self):
        """ inititialize function"""
        super().__init__()

    def put(self, key, item):
        """add items to dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get items from dictionary"""
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
