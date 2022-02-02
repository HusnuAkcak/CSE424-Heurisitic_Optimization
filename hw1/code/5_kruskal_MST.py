# Vertice numbers should start with 0
import random


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


class Graph:
    def __init__(self):
        self.graph = []
        self.verticeSet = {}
        self.cluster = []
        self.mst = []

    def add_edge(self, u, v, w):
        self.graph.append(Edge(u, v, w))

    def make_vertice_set(self):
        self.verticeSet = set([edge.u for edge in self.graph] + [edge.v for edge in self.graph])

    def cluster_vertices(self):
        for v in self.verticeSet:
            self.cluster.append([v, v])

    def sort(self):
        self.graph.sort(key=lambda edge: edge.w)

    def print(self):
        for e in self.graph:
            print(e.u, e.v, e.w)

    def kruskal(self):
        curr = 0
        while len(self.mst) < len(self.verticeSet) - 1 and curr < len(self.verticeSet):
            if not self.is_connected(self.graph[curr].u, self.graph[curr].v):
                self.connect(self.graph[curr].u, self.graph[curr].v)
                self.mst.append([self.graph[curr].u, self.graph[curr].v])
            curr+=1

    def is_connected(self, u, v):
        return self.cluster[u][1] == self.cluster[v][1]

    def connect(self, u, v):
        will_be_changed = self.cluster[v][1]
        for currV in self.cluster:
            if currV[1] == will_be_changed:
                currV[1] = self.cluster[u][1]


def generate_graph(num_of_vertex, max_cost):

    min_cost = 1
    g = Graph()
    # in this first loop we make sure that every vertex has a connection with graph
    for i in range(num_of_vertex-1):
        g.add_edge(i, i+1, random.randint(min_cost, max_cost))

    # this for loops are just adding random edges with random weighs
    for i in range(num_of_vertex):
        g.add_edge(i, random.randint(0, num_of_vertex-1), random.randint(min_cost, max_cost))

    for i in range(num_of_vertex):
        g.add_edge(i, random.randint(0, num_of_vertex-1), random.randint(min_cost, max_cost))

    return g


def get_graphs(num_of_graphs, max_edge_cost):

    gen_graphs = []
    for g_index in range(num_of_graphs):
        gen_graphs.append(generate_graph(g_index+1, max_edge_cost))

    return gen_graphs


def test1():
    g = Graph()

    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.sort()
    g.make_vertice_set()
    g.cluster_vertices()
    g.kruskal()

    print('===========================')
    g.print()
    print(g.mst)
    print('===========================')


def test2():

    g = Graph()

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 8)
    g.add_edge(0, 4, 22)
    g.add_edge(1, 2, 6)
    g.add_edge(4, 1, 11)
    g.add_edge(5, 4, 13)
    g.add_edge(2, 3, 8)
    g.add_edge(3, 4, 14)

    g.sort()
    g.make_vertice_set()
    g.cluster_vertices()
    g.kruskal()

    print('===========================')
    g.print()
    print(g.mst)
    print('===========================')


def test_many():
    graphs = get_graphs(50, 200)

    for g in graphs:
        g.sort()
        g.make_vertice_set()
        g.cluster_vertices()
        g.kruskal()
        print(g.mst)


test1()
test2()
# test_many()

