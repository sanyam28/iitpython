import time

class PriorityQueue:

  def __init__(self):
    self.heap = []

  def push(self, priority, item):
    self.heap.append((priority, item))
    self._up_heap(len(self.heap) - 1)

  def pop(self):
    if not self.heap:
      return None
    self._swap(0, len(self.heap) - 1)
    priority, item = self.heap.pop()
    self._down_heap(0)
    return priority, item

  def is_empty(self):
    return len(self.heap) == 0

  def _up_heap(self, index):
    parent = (index - 1) // 2
    if index > 0 and self.heap[index][0] < self.heap[parent][0]:
      self._swap(index, parent)
      self._up_heap(parent)

  def _down_heap(self, index):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if (
        left < len(self.heap)
        and self.heap[left][0] < self.heap[smallest][0]
    ):
      smallest = left
    if (
        right < len(self.heap)
        and self.heap[right][0] < self.heap[smallest][0]
    ):
      smallest = right

    if smallest != index:
      self._swap(index, smallest)
      self._down_heap(smallest)

  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class Graph:

  def __init__(self):
    self.adjacency_list = {}

  def add_node(self, node):
    if node not in self.adjacency_list:
      self.adjacency_list[node] = []

  def add_edge(self, u, v, weight):
    self.add_node(u)
    self.add_node(v)
    # Undirected connections between cities
    self.adjacency_list[u].append((v, weight))
    self.adjacency_list[v].append((u, weight))

  def dijkstra(self, start_node):
    """Computes shortest path from start_node to all other nodes using Dijkstra's algorithm."""
    distances = {node: float('inf') for node in self.adjacency_list}
    previous_nodes = {node: None for node in self.adjacency_list}

    distances[start_node] = 0
    pq = PriorityQueue()
    pq.push(0, start_node)

    visited = set()

    while not pq.is_empty():
      current_distance, current_node = pq.pop()

      if current_node in visited:
        continue
      visited.add(current_node)

      for neighbor, weight in self.adjacency_list[current_node]:
        distance = current_distance + weight

        if distance < distances[neighbor]:
          distances[neighbor] = distance
          previous_nodes[neighbor] = current_node
          pq.push(distance, neighbor)

    return distances, previous_nodes

  def get_shortest_path(self, start_node, target_node):
    """Reconstructs and prints the shortest path and distance."""
    distances, previous_nodes = self.dijkstra(start_node)

    path = []
    current = target_node

    while current is not None:
      path.append(current)
      current = previous_nodes[current]

    path.reverse()

    if path and path[0] == start_node:
      return path, distances[target_node]
    else:
      return [], float('inf')


g = Graph()

edges = [
    ('Shimla', 'Chandigarh', 112),
    ('Chandigarh', 'Ludhiana', 100),
    ('Chandigarh', 'Ambala', 45),
    ('Ludhiana', 'Ambala', 115),
    ('Ambala', 'Kurukshetra', 40),
    ('Ambala', 'Saharanpur', 65),
    ('Kurukshetra', 'Karnal', 35),
    ('Karnal', 'Panipat', 35),
    ('Panipat', 'Rohtak', 70),
    ('Panipat', 'New Delhi', 85),
    ('Panipat', 'Meerut', 75),
    ('Rohtak', 'Gurugram', 70),
    ('Rohtak', 'New Delhi', 65),
    ('New Delhi', 'Gurugram', 30),
    ('New Delhi', 'Meerut', 70),
    ('Saharanpur', 'Roorkee', 35),
    ('Saharanpur', 'Dehradun', 70),
    ('Dehradun', 'Rishikesh', 45),
    ('Roorkee', 'Rishikesh', 43),
    ('Roorkee', 'Dehradun', 52),
    ('Roorkee', 'Meerut', 110),
    ('Rishikesh', 'Haldwani', 210),
    ('Meerut', 'Haldwani', 200),
]

for u, v, weight in edges:
  g.add_edge(u, v, weight)


def display_result(start, destination):
  path, total_dist = g.get_shortest_path(start, destination)
  print(f'Shortest path from {start} to {destination}:')
  print(' -> '.join(path))
  print(f'Total Distance: {total_dist} km\n')

start = time.time()
display_result('Shimla', 'Gurugram')
display_result('Haldwani', 'Chandigarh')
end = time.time()
print(end-start)