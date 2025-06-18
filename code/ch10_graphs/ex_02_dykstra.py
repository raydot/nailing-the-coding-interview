# ex_02_dykstra.py

import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start, end):
    """
    Implementation of Dijkstra's algorithm to find shortest path
    from start node to end node in a weighted graph.
    
    Args:
        graph: Dictionary representing the weighted graph as adjacency list
        start: Starting node
        end: Destination node
        
    Returns:
        Tuple of (shortest distance, path as a list)
    """
    # Priority queue for (distance, node) pairs
    # We'll use it to always process the closest unvisited node first
    priority_queue = [(0, start, [])]
    
    # Dictionary to track the shortest distance to each node
    shortest_distances = {start: 0}
    
    # Dictionary to track visited nodes
    visited = set()
    
    while priority_queue:
        # Get the node with the smallest distance so far
        current_distance, current_node, path = heapq.heappop(priority_queue)
        
        # If we've reached our destination, we're done
        if current_node == end:
            return current_distance, path + [current_node]
        
        # If we've already processed this node, skip it
        if current_node in visited:
            continue
        
        # Mark current node as visited
        visited.add(current_node)
        
        # Check all neighbors
        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue
                
            # Calculate distance to neighbor
            distance = current_distance + weight
            
            # If we found a shorter path to the neighbor, update it
            if neighbor not in shortest_distances or distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor, path + [current_node]))
    
    # If we get here, there's no path to the end node
    return float('inf'), []

def display_graph(graph, path=None):
    """
    Visualizes the graph and highlights the shortest path if provided
    """
    G = nx.DiGraph()
    
    # Add edges with weights
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)
    
    # Position nodes using spring layout
    pos = nx.spring_layout(G, seed=42)
    
    # Draw the graph
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', 
            font_size=15, font_weight='bold', arrows=True)
    
    # Draw edge weights
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
    
    # Highlight the shortest path if provided
    if path and len(path) > 1:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red')
    
    plt.title("Dijkstra's Algorithm Demonstration", fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def main():
    # Define our graph - using the example from your text
    # Each node maps to a dictionary of {neighbor: distance}
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 1, 'D': 5},
        'C': {'B': 1, 'D': 8, 'E': 10},
        'D': {'E': 2, 'F': 6},
        'E': {'F': 3},
        'F': {}
    }
    
    # Choose start and end nodes
    start_node = 'A'
    end_node = 'F'
    
    print(f"Finding shortest path from {start_node} to {end_node}...")
    distance, path = dijkstra(graph, start_node, end_node)
    
    if distance != float('inf'):
        print(f"Shortest distance: {distance}")
        print(f"Shortest path: {' -> '.join(path)}")
    else:
        print(f"No path exists from {start_node} to {end_node}")
    
    # Visualize the graph and the shortest path
    display_graph(graph, path)

if __name__ == "__main__":
    main()