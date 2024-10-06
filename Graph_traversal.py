from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Add an edge to the graph (u -> v)."""
        self.graph[u].append(v)

    def dfs(self, start):
        """Perform Depth First Search (DFS) from a starting node."""
        visited = set()  # To track visited nodes
        self._dfs_util(start, visited)

    def _dfs_util(self, node, visited):
        """Utility function for DFS (recursive)."""
        visited.add(node)
        print(node, end=' ')  # Print current node

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)

    def bfs(self, start):
        """Perform Breadth First Search (BFS) from a starting node."""
        visited = set()  # To track visited nodes
        queue = deque([start])

        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=' ')  # Print current node

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

def main():
    g = Graph()

    # Adding edges to the graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Depth First Search (DFS) starting from node 2:")
    g.dfs(2)  # DFS starting from node 2
    print("\n")

    print("Breadth First Search (BFS) starting from node 2:")
    g.bfs(2)  # BFS starting from node 2
    print("\n")

if __name__ == "__main__":
    main()
