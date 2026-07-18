from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        # self.queue = deque()
        self.cache = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        val= self.cache[key]
        del self.cache[key]
        self.cache[key]= val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache[key]= value
        else:
            if len(self.cache)!=self.capacity:
                self.cache[key]= value
                
            else:
                least_prior = next(iter(self.cache))
                del self.cache[least_prior]
                self.cache[key]=value
