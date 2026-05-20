from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        # Add new request
        self.queue.append(t)

        # Remove requests older than t - 3000
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        # Return number of recent requests
        return len(self.queue)