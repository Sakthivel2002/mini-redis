import time
import threading
from lru import LRUCache


class Store:
    def __init__(self, max_keys=100):
        self.data = LRUCache(max_keys)
        self.expiry = {}

        cleanup_thread = threading.Thread(target=self._cleanup_worker, daemon=True)
        cleanup_thread.start()

    def set(self, key, value, ttl=None):

        evicted = self.data.put(key, value)

        if evicted:
            if evicted in self.expiry:
                del self.expiry[evicted]

        if ttl:
            self.expiry[key] = time.time() + ttl
        elif key in self.expiry:
            del self.expiry[key]

        return "OK"

    def get(self, key):

        if self._is_expired(key):
            self.delete(key)
            return None

        return self.data.get(key)

    def delete(self, key):

        self.data.delete(key)

        if key in self.expiry:
            del self.expiry[key]

        return 1

    def ttl(self, key):

        if key not in self.expiry:
            return -1

        remaining = int(self.expiry[key] - time.time())

        if remaining <= 0:
            self.delete(key)
            return -2

        return remaining

    def _is_expired(self, key):

        if key not in self.expiry:
            return False

        return time.time() > self.expiry[key]

    def _cleanup_worker(self):
        while True:
            time.sleep(5)

            now = time.time()

            for key in list(self.expiry.keys()):
                if now > self.expiry[key]:
                    self.delete(key)