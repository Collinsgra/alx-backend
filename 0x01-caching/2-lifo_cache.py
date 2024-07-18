#!/usr/bin/python3
""" Last in First Out Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Last in First Out caching """

    def __init__(self):
        """ script """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Puts items to cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.queue:
                last = self.queue.pop()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.mv_last_list(key)

    def get(self, key):
        """ Gets items """
        return self.cache_data.get(key, None)

    def mv_last_list(self, item):
        """ Moves elements """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)
