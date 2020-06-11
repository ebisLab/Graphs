"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


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

    # version 2 -> ONLY CONNECTING TO VERTS THAT EXIST
    def add_edge(self, v1, v2):  # add 1 vert iD to the set of the source vertex
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)  # add v2 as a neighbor to v1
        else:
            raise IndexError("Vertex does not exist")

    # get neighbors for a vert

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex. (TRAVERSAL TO ADD THEM TO THE LIST)
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # set
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex_id)
        # create a set to store visited vertices
        visited = set()
        # while the quue is not empty...
        while q.size() > 0:
            # dequue the first vertex
            v = q.dequeue()
        # if that vertex has not been visited...
            if v not in visited:
                # visit it -> do whatever you have to do depending on the goal
                print(v)
            # mark it as visitied
                visited.add(v)  # add it to the set
        # then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex_id):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # use stack, enqueue becomes push, dequue becomes pop
        q = Stack()
        q.push(starting_vertex_id)
        # create a set to store visited vertices
        visited = set()
        # while the quue is not empty...
        while q.size() > 0:
            # dequue the first vertex
            v = q.pop()
        # if that vertex has not been visited...
            if v not in visited:
                # visit it -> do whatever you have to do depending on the goal
                print(v)
        # mark it as visitied
                visited.add(v)  # add it to the set
        # then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()  # need a way to pass that around

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex_id, destination_vertex_id):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
    # Create an empty queue and enqueue A PATH TO the starting vertex ID:
        q = Queue()
        q.enqueue([starting_vertex_id])
    # Create a Set to store visited vertices
        visited = set()

    # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            p = q.dequeue()

        # Grab the last vertex from the PATH
            vertex = p[-1]
        # If that vertex has not been visited...
            if vertex not in visited:
             # CHECK IF IT'S THE TARGET
                if vertex == destination_vertex_id:
                    # IF SO, RETURN PATH
                    return p
                else:
                    # Mark it as visited...
                    visited.add(vertex)  # add it to the set

                # Then add A PATH TO its neighbors to the back of the queue
                neighbors = self.get_neighbors(vertex)

                for neighbor in neighbors:
                    # COPY THE PATH
                    new_path = list(p)
                    # APPEND THE NEIGHOR TO THE BACK
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex_id, destination_vertex_id):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO
    # Create an empty queue and enqueue A PATH TO the starting vertex ID:
        q = Stack()
        q.push([starting_vertex_id])
    # Create a Set to store visited vertices
        visited = set()

    # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            p = q.pop()

        # Grab the last vertex from the PATH
            vertex = p[-1]
        # If that vertex has not been visited...
            if vertex not in visited:
             # CHECK IF IT'S THE TARGET
                if vertex == destination_vertex_id:
                    # IF SO, RETURN PATH
                    return p
                else:
                    # Mark it as visited...
                    visited.add(vertex)  # add it to the set

                # Then add A PATH TO its neighbors to the back of the stack
                neighbors = self.get_neighbors(vertex)

                for neighbor in neighbors:
                    # COPY THE PATH
                    new_path = list(p)
                    # APPEND THE NEIGHOR TO THE BACK
                    new_path.append(neighbor)
                    q.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()  # need a way to pass that around

        if path is None:
            path = []

        if starting_vertex not in visited:
            # searching

            visited.add(starting_vertex)
            # when we reach the destination

            # try to update your path to include current vertex
            path = [*path, starting_vertex]  # *path => ...
            if starting_vertex == destination_vertex:
                return path

            for neighbor in self.get_neighbors(starting_vertex):
                result = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path)
                if result:
                    return result

                # if neighbor finds path, it will return path to
                # passby val, passby ref


g = Graph()

g.add_vertex('A')
g.add_vertex('B')  # B is its ID #1. Doesnt have edges
g.add_vertex('C')
g.add_vertex('E')

g.add_edge('B', 'C')  # One direction
g.add_edge('C', 'B')  # Bi directional
g.add_edge('B', 'A')  # One direction
g.add_edge('B', 'E')  # One direction
# g.add_edge('B', 'F')  # One direction


print(g.get_neighbors('B'))
print(g.get_neighbors('C'))
print("----------")
print(g.vertices)

print("----------")
print("GET BREADTH FIRST")
# decide where to start from
g.bft('A')  # not connected to anything
print('..')
g.bft('B')
print("-------")
print("GET DEPTH FIRST")
g.dft('A')

print("-----")
print("GET BREADTH FIRST SEARCH")
print(g.vertices)

# g.bfs(1, 6)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
