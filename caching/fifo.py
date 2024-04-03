class CacheFIFO: 
    def __init__(self, capacity): 
        self.cache = [] 
        self.capacity = capacity 
    
    def get(self, key): 
        # Code to fetch data from the cache pass 
        pass
    
    def put(self, key, value): 
        if len(self.cache) >= self.capacity: 
            # Evict the first item from the cache (FIFO) 
            self.cache.pop(0) 
        self.cache.append((key, value))

