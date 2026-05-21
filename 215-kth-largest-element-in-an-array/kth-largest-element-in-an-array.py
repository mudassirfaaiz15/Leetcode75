import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            # Keep heap size equal to k
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]