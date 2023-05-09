from controller.Grafo import Grafo

grafo = Grafo()

grafo.ingresarVertices("MANIZALES")
grafo.ingresarVertices("IBAGUE")
grafo.ingresarArista("MANIZALES","IBAGUE",1)
grafo.showVertices()
grafo.showAristas()