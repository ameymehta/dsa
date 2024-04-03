import heapq

class KthLargest:
    def __init__(self, k, nums) -> None:
        self.top_k_nums_heap = []
        self.k = k

        for element in nums:
            self.add(element)

    def add(self, val):
        if len(self.top_k_nums_heap) < self.k:
            heapq.heappush(self.top_k_nums_heap, val)
        elif val > self.top_k_nums_heap[0]:
            heapq.heappop(self.top_k_nums_heap)
            heapq.heappush(self.top_k_nums_heap, val)
        return self.top_k_nums_heap[0]
    
# Driver code
def main():
    nums = [3, 6, 9, 10]
    temp = [3, 6, 9, 10]
    print("Initial stream: ", nums, sep = "")
    print("k: ", 3, sep = "")
    k_largest = KthLargest(3, nums)
    val = [4, 7, 10, 8, 15]
    for i in range(len(val)):
        print("\tAdding a new number ", val[i], " to the stream", sep = "")
        temp.append(val[i])
        print("\tNumber stream: ", temp, sep = "")
        print("\tKth largest element in the stream: ", k_largest.add(val[i]))
        print("---")

if __name__ == "__main__":
    main()
