import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        pairs = sorted(zip(nums2, nums1), reverse=True)

        min_heap = []
        current_sum = 0
        answer = 0

        for n2, n1 in pairs:
            heapq.heappush(min_heap, n1)
            current_sum += n1

            # Keep only k elements
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)

            # Calculate score when heap size becomes k
            if len(min_heap) == k:
                answer = max(answer, current_sum * n2)

        return answer