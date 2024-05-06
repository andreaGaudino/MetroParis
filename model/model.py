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
        self.addEdgeMode3()

    def addEdgeMode3(self):
        #Mode 3: unica query che legge tutte le connessioni
        self._grafo.clear_edges()
        allConnessioni = DAO.getAllConnessioni()
        # print(len(allConnessioni))
        for c in allConnessioni:
            u_nodo = self._idMap[c.id_stazP]
            v_nodo = self._idMap[c.id_stazA]
            self._grafo.add_edge(u_nodo, v_nodo)
            # print(f"Added edge between {u_nodo} and {v_nodo}")

    def addEdgeMode1(self):
        # Mode 1: doppio loop su nodi e query per ogni arco.
        self._grafo.clear_edges()
        for u in self._fermate:
            for v in self._fermate:
                res = DAO.getEdge(u,v)
                if len(res)>0:
                    self._grafo.add_edge(u,v)
                    # print(f"Added edge between {u} and {v}")

    def addEdgeMode2(self):
        # Mode 2: loop singolo sui nodi e query per identificare i vicini
        self._grafo.clear_edges()
        for u in self._fermate:
            vicini = DAO.getEdgesVicini(u)
            for v in vicini:
                v_nodo = self._idMap[v.id_stazA]
                self._grafo.add_edge(u,v_nodo)
                # print(f"Added edge between {u} and {v_nodo}")

    @property
    def fermate(self):
        return self._fermate

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)
