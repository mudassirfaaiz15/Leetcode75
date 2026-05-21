import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        n = len(costs)

        left_heap = []
        right_heap = []

        left = 0
        right = n - 1

        # Fill initial candidates from left
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, costs[left])
                left += 1

        # Fill initial candidates from right
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(right_heap, costs[right])
                right -= 1

        total = 0

        for _ in range(k):

            left_min = left_heap[0] if left_heap else float('inf')
            right_min = right_heap[0] if right_heap else float('inf')

            # Choose smaller cost
            if left_min <= right_min:
                total += heapq.heappop(left_heap)

                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                total += heapq.heappop(right_heap)

                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1

        return total