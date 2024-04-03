from heapq import *

# For reference, here are the Rankable and DataSource interfaces.
# You do not need to implement them, and should not make assumptions
# about their implementations.
class Rankable:
    # Returns the Rank of this object, using some algorithm and potentially
    # the internal state of the Rankable.
    def getRank() -> int:
        pass
 
 
class DataSource:
    def get(key: K) -> Rankable:
        pass

 
# Class we're actually implementing:
class RetainBestCache:
    # Constructor with a data source (assumed to be slow) and a cache size
    # @param data_source the persistent layer of the the cache
    # @param entries_to_retain the number of entries that the cache can hold
    def __init__(self, data_source: DataSource, entries_to_retain: int) -> None:
        self.keyDict = {}
        self.data_source = data_source
        self.limit = entries_to_retain
        self.minHeap = []
        self.rankDict = {}
 
    # Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
    # retrieves it from the data source. If the cache is full, attempt to cache the returned data,
    # evicting the V with lowest rank among the ones that it has available
    # If there is a tie, the cache may choose any V with lowest rank to evict.
    # @param key the key of the cache entry being queried
    # @return the Rankable value of the cache entry
    def get(self, key: K) -> Rankable:
        if k in self.keyDict:
            return self.keyDict[k]
        else:
            data = self.data_source.get(k)
            if data:
                sync:
                    if len(self.keyDict) == self.limit:
                        lowestRank = self.minHeap[0]
                        kForLowestRank = self.rankDict[lowestRank]
                        del self.keyDict[kForLowestRank]
                        del self.rankDict[lowestRank]
                        heappop(minHeap)
                    self.keyDict[k] = data
                    rank = data.getRank()
                    self.rankDict[rank] = k
                    heappush(minHeap, rank)
                    return data
            else:
                return null

"""
test case example:
data_store:
"A" => rank 2
"B" => rank 3
entries_to_retain = 1

assert cache.get("A") = rank 2
assert_cache_miss()
assert cache.get("A") = rank 2
asset_cache_exists()
assert cache.get("B") = rank 3
assert cache.get("C") = null

"""