from controller.Grafo import Grafo

grafo = Grafo()

# ingreso de vertices
grafo.ingresarVertices("MANIZALES")
grafo.ingresarVertices("MEDELLIN")
grafo.ingresarVertices("SANTA MARTA")
grafo.ingresarVertices("CARTAGO")
grafo.ingresarVertices("VILLAMARIA")
grafo.ingresarVertices("CHINCHINA")
grafo.ingresarVertices("SUPIA")
grafo.ingresarVertices("BOGOTA")

# ingreso de aristas no dirigidas
grafo.ingresarArista("MANIZALES", "VILLAMARIA", 9)
grafo.ingresarArista("VILLAMARIA", "SANTA MARTA", 10)

grafo.ingresarArista("CHINCHINA", "SANTA MARTA", 8)
grafo.ingresarArista("CHINCHINA", "VILLAMARIA", 2)

grafo.ingresarArista("SUPIA", "CHINCHINA", 1)
grafo.ingresarArista("SUPIA", "CARTAGO", 4)

grafo.ingresarArista("CARTAGO", "SANTA MARTA", 7)
grafo.ingresarArista("MEDELLIN", "SANTA MARTA", 6)

grafo.ingresarArista("MEDELLIN", "CARTAGO", 3)
grafo.ingresarArista("CARTAGO", "BOGOTA", 5)


# pruebas

# grafo.showAristas()
grafo.showListsAdy()
# grafo.verticesFuente()
# grafo.verticesPozo()
grafo.recorridoEnProfundidad("CARTAGO")
grafo.recorridoEnAmplitud("CARTAGO")