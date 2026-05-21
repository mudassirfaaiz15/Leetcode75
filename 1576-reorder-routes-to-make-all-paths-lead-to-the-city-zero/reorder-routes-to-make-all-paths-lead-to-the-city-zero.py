from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)

        # Build graph
        for a, b in connections:
            graph[a].append((b, 1))  # original direction
            graph[b].append((a, 0))  # reverse direction

        visited = set()
        changes = 0

        # BFS from city 0
        queue = deque([0])
        visited.add(0)

        while queue:
            city = queue.popleft()

            for nei, cost in graph[city]:
                if nei not in visited:
                    visited.add(nei)
                    changes += cost
                    queue.append(nei)

        return changes