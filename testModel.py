from model.model import Model

mymodel = Model()
mymodel.buildGraph()

print(f"il grafo ha {mymodel.getNumNodes()} nodi")
for i in mymodel._grafo.edges:
    print(i[0]._nome, "---",i[1]._nome)