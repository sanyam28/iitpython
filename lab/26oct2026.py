#Graphs

class Node:
    def __init__(self, val):
        self.value = val

class Edge:
    def __init__(self, ori, dest):
        self.ori = ori
        self.dest = dest

class Graphs:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            print("Node is already Present")
            return
        else:
            self.nodes.append(node)
            self.edges[node] = []
            
    def addEdge(self,edge):
        self.edges[edge.ori].append(edge.dest)

        
    def display(self):
        for node in self.nodes:
            print(node, ":", end=" ")
            for edge in self.edges:
                if edge.ori == node:
                    print(edge.dest, end=" ")
            print()

    # def path(self, ori, dest):
    # depth first search- guttag book
    # breadth first search- guttag book


g = Graphs()
g.display()