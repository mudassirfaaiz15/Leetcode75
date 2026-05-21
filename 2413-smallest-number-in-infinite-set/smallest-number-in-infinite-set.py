import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.heap = []
        self.added = set()

    def popSmallest(self) -> int:
        # Return smallest added-back number first
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.added.remove(smallest)
            return smallest

        # Otherwise return current smallest
        val = self.current
        self.current += 1
        return val

    def addBack(self, num: int) -> None:
        # Only add back if it was already removed
        # and not already present in heap
        if num < self.current and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)