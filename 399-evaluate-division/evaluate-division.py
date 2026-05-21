from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        # Build graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0

            if src == dst:
                return 1.0

            queue = deque([(src, 1.0)])
            visited = set([src])

            while queue:
                node, product = queue.popleft()

                if node == dst:
                    return product

                for nei, weight in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, product * weight))

            return -1.0

        result = []

        for c, d in queries:
            result.append(bfs(c, d))

        return result