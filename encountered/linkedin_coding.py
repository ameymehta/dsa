# Interfaces of existing objects, for reference:
class Rankable:
  def getRank() -> int:
    pass
 
 
class DataSource:
  def get(key: K) -> Rankable:
    pass
 

# Class we're actually implementing:
class RetainBestCache:
  def __init__(self, data_source: DataSource, entries_to_retain: int) -> None:
    # 1 hashmaps => (key, value) and 1 heap for (rank, key)
    self.cacheMap = {}
    self.maxHeap = [] # size of maxHeap 
    self.data_source = data_source
    self.entries_to_retain = entries_to_retain
    pass
 
  def get(self, key: K) -> Rankable:
    # if in cache, return value from cache
    if K in self.cacheMap:
        return self.cacheMap[key]
    
    # if not in cache, fetch from the orignal source, and add to the cache, also if cache is full, remove least ranked item
    else:
        return put(self, key: K)
    
  def put(self, key: K):
    # fetch from the original source, add to the cache
    item = self.data_source.get(key)
    if len(self.cacheMap) >= self.entries_to_retain:
        # evict form the cache
        rank = -self.maxHeap.popleft()
        cacheMap.delete(key)
    # add to cache
    newRank = item.value.getRank()
    self.maxHeap.append(newRank)
    self.maxHeap.heapify()
    cacheMap[item.key] = item.value
    return item
        
    