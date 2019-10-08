"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        # self.visited = set()

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError("Cannot create an edge based on given vertices.")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            vertex = queue.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for next_vert in self.vertices[vertex]:
                    queue.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # From the starting vertex
        # pass in each child vertex to dft_recursive
        # if visited == None:
        #     visited = set()
        
        # if starting_vertex in visited:
        #     return

        
        print(starting_vertex)
        visited.add(starting_vertex)

        for next_vert in self.vertices[starting_vertex]:
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        if starting_vertex == destination_vertex:
            print(starting_vertex)
            return

        queue = Queue()
        visited = set()
        previous = {}
        queue.enqueue([starting_vertex])

        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    next_path = list(path)
                    next_path.append(next_vert)
                    queue.enqueue(next_path)

        # while queue.size() > 0:
        #     vertex = queue.dequeue()
            
        #     if vertex not in visited:
        #         visited.add(vertex)
        #         if vertex == destination_vertex:
        #             current_vert = destination_vertex
        #             path = []
        #             while current_vert != starting_vertex:
        #                 path.append(current_vert)
        #                 current_vert = previous[current_vert]
        #             path.append(starting_vertex)
        #             path.reverse()
        #             return path

        #         for next_vert in self.vertices[vertex]:
        #             if not next_vert in previous:
        #                 previous[next_vert] = vertex
        #             queue.enqueue(next_vert)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        previous = {}

        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                if vertex == destination_vertex:
                    current_vert = destination_vertex
                    path = []
                    while current_vert != starting_vertex:
                        path.append(current_vert)
                        current_vert = previous[current_vert]
                    path.append(starting_vertex)
                    path.reverse()
                    return path
                
                for next_vert in self.vertices[vertex]:
                    if not next_vert in previous:
                        previous[next_vert] = vertex
                    stack.push(next_vert)




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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("starting dft")
    graph.dft(1)

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
    print("starting bft")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("starting dft recursive")
    graph.dft_recursive(1)
    print("starting dft recursive 2")
    graph.dft_recursive(2)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("starting breadth first search")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("starting depth first search")
    print(graph.dfs(1, 6))
