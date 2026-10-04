import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums          # Store the numbers in a min-heap
        self.k = k                   # We want the kth-largest number

        heapq.heapify(self.minHeap)  # Convert nums into a min-heap in O(n)

        # Keep only the k largest elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # Remove the smallest element

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)  # Add the new number

        # If we have more than k elements, remove the smallest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The smallest of our k largest elements is the kth largest overall
        return self.minHeap[0]