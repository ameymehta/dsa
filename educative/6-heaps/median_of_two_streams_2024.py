from heapq import *

class MedianOfStream:
    max_heap = []
    min_heap = []

    def insert_num(self, n):
        if not self.max_heap or -self.max_heap[0] > n:
            heappush(self.max_heap, -n)
        else:
            heappush(self.min_heap, n)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
        
    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0]/2.0 + self.min_heap[0]/2.0
        else:
            return -self.max_heap[0]/1.0
    
# Driver code
def main():
    median_num = MedianOfStream()
    nums = [35, 22, 30, 25, 1]
    numlist = []
    x = 1
    for n in nums:
        numlist.append(n)
        print(x, ".\tData stream: ", numlist, sep="")
        median_num.insert_num(n)
        print("\tThe median for the given numbers is: " +
              str(median_num.find_median()), sep="")
        print("---")
        x += 1


if __name__ == "__main__":
    main()