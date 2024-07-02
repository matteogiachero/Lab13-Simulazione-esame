from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._listSighting = []
        self._listShape = []
        self._listStates = []

        self._grafo = nx.Graph()
        self._nodes = []
        self._edges = []

        self.loadSighting()
        self.loadShapes()
        self.loadStates()

    def loadSighting(self):
        self._listSighting = DAO.getAllSighting()

    def loadShapes(self):
        self._listShape = DAO.getAllShapes()

    def loadStates(self):
        self._listStates = DAO.getAllStates()

    @property
    def listSighting(self):
        return self._listSighting

    @property
    def listShape(self):
        return self._listShape

    @property
    def listStates(self):
        return self._listStates

    def buildGraph(self, s, a):
        self._grafo.clear()
        print(a, s)

        for p in self._listStates:
            self._nodes.append(p)

        self._grafo.add_nodes_from(self._nodes)
        self.idMap = {}
        for n in self._nodes:
            self.idMap[n.id] = n

        tmp_edges = DAO.getAllWeightedNeigh(a, s)

        for e in tmp_edges:
            self._edges.append((self.idMap[e[0]], self.idMap[e[1]], e[2]))

        self._grafo.add_weighted_edges_from(self._edges)

    def get_sum_weight_per_node(self):
        pp = []
        for n in self._grafo.nodes():
            sum_w = 0
            for e in self._grafo.edges(n, data=True):
                sum_w += e[2]['weight']
            pp.append((n.id, sum_w))
        return pp

    def get_nodes(self):
        return self._grafo.nodes()

    def get_edges(self):
        return list(self._grafo.edges(data=True))

    def get_num_of_nodes(self):
        return self._grafo.number_of_nodes()

    def get_num_of_edges(self):
        return self._grafo.number_of_edges()

