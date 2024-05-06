from model.model import Model

mymodel = Model()
mymodel.buildGraph()

print(f"il grafo ha {mymodel.getNumNodes()} nodi")