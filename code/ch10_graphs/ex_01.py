class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        """Add a new vertex to the graph if it doesn't exist already"""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        """Add an undirected edge between vertex1 and vertex2"""
        # Make sure both vertices exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        # Add the edge in both directions (undirected graph)
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
        if vertex1 not in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)
    
    def display(self):
        """Display the graph structure"""
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {', '.join(map(str, neighbors))}")
            
    def depth_first_traversal(self, start, visited=None):
      if visited is None:
        visited = set()
      
      visited.add(start)
      print(start)
      
      for neighbor in self.graph[start]:
        if neighbor not in visited:
          self.depth_first_traversal(neighbor, visited)
          
    def breadth_first_traversal(self, start):
      visited = set()
      queue = [start]
      
      while queue:
          vertex = queue.pop(0)
          if vertex not in visited:
              visited.add(vertex)
              print(vertex)
              queue.extend(neighbor for neighbor in self.graph[vertex] if neighbor not in visited)





# Create the graph
g = Graph()

# Add edges (connections between people)
g.add_edge('Amir', 'Beth')
g.add_edge('Amir', 'Chen')
g.add_edge('Amir', 'Diego')
g.add_edge('Beth', 'Emma')
g.add_edge('Beth', 'Farid')
g.add_edge('Chen', 'Gina')
g.add_edge('Diego', 'Hiroshi')
g.add_edge('Emma', 'Ian')
g.add_edge('Farid', 'Jamal')
g.add_edge('Gina', 'Kyle')

# Display the graph structure
print("Social Connections:")
g.display()

# Perform depth-first traversal starting from 'Amir'
print("\nDepth-First Traversal starting from 'Amir':")
g.depth_first_traversal('Amir')

# Perform breadth-first traversal starting from 'Amir'
print("\nBreadth-First Traversal starting from 'Amir':")
g.breadth_first_traversal('Amir')