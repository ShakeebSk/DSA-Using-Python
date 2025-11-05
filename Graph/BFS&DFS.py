
class Graph:
    """Graph implementation using adjacency list"""
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
        self.vertices = set()
    
    def add_vertex(self, v):
        """Add a vertex to the graph"""
        self.vertices.add(v)
        if v not in self.graph:
            self.graph[v] = []
    
    def add_edge(self, u, v, weight=1):
        """Add an edge between vertices u and v"""
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def get_vertices(self):
        """Get all vertices in the graph"""
        return list(self.vertices)
    
    def get_edges(self):
        """Get all edges in the graph"""
        edges = []
        for u in self.graph:
            for v, w in self.graph[u]:
                if self.directed or (v, u, w) not in edges:
                    edges.append((u, v, w))
        return edges
    
    def get_neighbors(self, v):
        """Get neighbors of vertex v"""
        return [neighbor for neighbor, _ in self.graph[v]]
    
    def bfs(self, start):
        """Breadth-First Search - returns visit order and parent map"""
        visited = set()
        queue = deque([start])
        visit_order = []
        parent = {start: None}
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                visit_order.append(vertex)
                
                for neighbor, _ in self.graph[vertex]:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
                        if neighbor not in parent:
                            parent[neighbor] = vertex
        
        return visit_order, parent
    
    def bfs_with_levels(self, start):
        """BFS with level information"""
        visited = set([start])
        queue = deque([(start, 0)])
        visit_order = []
        levels = {start: 0}
        
        while queue:
            vertex, level = queue.popleft()
            visit_order.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
                    levels[neighbor] = level + 1
        
        return visit_order, levels
    
    def dfs(self, start):
        """Depth-First Search - returns visit order and parent map"""
        visited = set()
        visit_order = []
        parent = {start: None}
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            visit_order.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    parent[neighbor] = vertex
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return visit_order, parent
    
    def dfs_iterative(self, start):
        """Iterative DFS using stack"""
        visited = set()
        stack = [start]
        visit_order = []
        parent = {start: None}
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                visit_order.append(vertex)
                
                # Add neighbors in reverse to maintain left-to-right order
                neighbors = [n for n, _ in self.graph[vertex]]
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        if neighbor not in parent:
                            parent[neighbor] = vertex
        
        return visit_order, parent
    
    def is_connected(self):
        """Check if graph is connected (for undirected graphs)"""
        if not self.vertices:
            return True
        start = next(iter(self.vertices))
        visit_order, _ = self.bfs(start)
        return len(visit_order) == len(self.vertices)
    
    def has_cycle_undirected(self):
        """Detect cycle in undirected graph using DFS"""
        visited = set()
        
        def dfs_cycle(vertex, parent):
            visited.add(vertex)
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs_cycle(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        for vertex in self.vertices:
            if vertex not in visited:
                if dfs_cycle(vertex, None):
                    return True
        return False
    
    def has_cycle_directed(self):
        """Detect cycle in directed graph using DFS"""
        visited = set()
        rec_stack = set()
        
        def dfs_cycle(vertex):
            visited.add(vertex)
            rec_stack.add(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs_cycle(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(vertex)
            return False
        
        for vertex in self.vertices:
            if vertex not in visited:
                if dfs_cycle(vertex):
                    return True
        return False
    
    def shortest_path_bfs(self, start, end):
        """Find shortest path using BFS (for unweighted graphs)"""
        if start not in self.vertices or end not in self.vertices:
            return None
        
        visited = set([start])
        queue = deque([(start, [start])])
        
        while queue:
            vertex, path = queue.popleft()
            
            if vertex == end:
                return path
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None
    
    def connected_components(self):
        """Find all connected components"""
        visited = set()
        components = []
        
        for vertex in self.vertices:
            if vertex not in visited:
                component, _ = self.bfs(vertex)
                components.append(component)
                visited.update(component)
        
        return components
    
    def topological_sort(self):
        """Topological sort for directed acyclic graph (DAG)"""
        if not self.directed:
            return None
        
        visited = set()
        stack = []
        
        def dfs_topo(vertex):
            visited.add(vertex)
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_topo(neighbor)
            stack.append(vertex)
        
        for vertex in self.vertices:
            if vertex not in visited:
                dfs_topo(vertex)
        
        return stack[::-1]


class WeightedGraph(Graph):
    """Extended graph class with weighted edge algorithms"""
    
    def dijkstra(self, start):
        """Dijkstra's shortest path algorithm"""
        distances = {v: float('infinity') for v in self.vertices}
        distances[start] = 0
        visited = set()
        parent = {start: None}
        
        while len(visited) < len(self.vertices):
            # Find unvisited vertex with minimum distance
            current = None
            min_dist = float('infinity')
            for v in self.vertices:
                if v not in visited and distances[v] < min_dist:
                    min_dist = distances[v]
                    current = v
            
            if current is None:
                break
            
            visited.add(current)
            
            # Update distances to neighbors
            for neighbor, weight in self.graph[current]:
                if neighbor not in visited:
                    new_dist = distances[current] + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        parent[neighbor] = current
        
        return distances, parent
    
    def bellman_ford(self, start):
        """Bellman-Ford algorithm (handles negative weights)"""
        distances = {v: float('infinity') for v in self.vertices}
        distances[start] = 0
        parent = {start: None}
        
        # Relax edges V-1 times
        for _ in range(len(self.vertices) - 1):
            for u in self.graph:
                for v, weight in self.graph[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        parent[v] = u
        
        # Check for negative cycles
        for u in self.graph:
            for v, weight in self.graph[u]:
                if distances[u] + weight < distances[v]:
                    return None, None  # Negative cycle detected
        
        return distances, parent
