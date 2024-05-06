from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMap = {}
        for f in self._fermate:
            self._idMap[f.id_fermata] = f

    def buildGraph(self):
        self._grafo.add_nodes_from(self._fermate)

        for u in self._fermate:
            vicini = None
            for v in self._fermate:
                v_nodo = self._idMap[v.]
                res = DAO.getEdge(u,v)

                if len(res) > 0:
                    self._grafo.add_edge(u, v)
                    #print(f"Added edge between {u} and {v}")

    @property
    def fermate(self):
        return self._fermate

    def getNumNodes(self):
        return len(self._fermate)
    def getNumEdges(self):
        return len(self._grafo)