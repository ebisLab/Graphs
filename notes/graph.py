class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Add it straight to the graph
        # set of edges from this vert # BY DEFAULT ITS EMPTY
        self.vertices[vertex_id] = set()
        # set() is working as a list, you cant have duplicates

    def add_edge(self, v1, v2):  # add 1 vert iD to the set of the source vertex
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)  # add v2 as a neighbor to v1

    # get neighbors for a vert

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex. (TRAVERSAL TO ADD THEM TO THE LIST)
        """
        return self.vertices[vertex_id]


g = Graph()

g.add_vertex('B')  # B is its ID #1. Doesnt have edges
g.add_vertex('C')

g.add_edge('B', 'C')  # One direction
g.add_edge('C', 'B')  # Bi directional

print(g.get_neighbors('B'))
