from model.Vertice import Vertice
from model.Arista import Arista
from collections import deque

class Grafo:
    
    '''DEFINE AL GRAFO CON UNA LISTA VACÍA DE VERTICES Y ARISTAS'''
    def __init__(self):
        self.list_vertices = []
        self.list_aristas = []
        
    '''MÉTODOS PARA INGRESAR VERTICES AL GRAFO'''
    def ingresarVertices(self, data):
        if self.verificarExistenciaVertice(data, self.list_vertices) != True:
            self.list_vertices.append(Vertice(data))
        
    def verificarExistenciaVertice(self, data, list):
        for i in range(len(list)):
            if data == list[i].getData():
                return True
        return False
    
    '''METODOS PARA INGRESAR ARISTAS'''
    def ingresarArista(self, origen, destino, peso):
        if not self.verificarExistenciaArista(origen, destino, self.list_aristas):
            if self.verificarExistenciaVertice(origen, self.list_vertices) and self.verificarExistenciaVertice(destino, self.list_vertices):
                self.list_aristas.append(Arista(origen, destino, peso))
                # self.list_aristas.append(Arista(destino, origen, peso))
                self.obtenerVertice(origen).getListAdy().append(destino)
                # self.obtenerVertice(destino).getListAdy().append(origen)
          
    def verificarExistenciaArista(self, origen, destino, lista):
        for i in range(len(lista)):
            if origen == lista[i].getOrigen() and destino == lista[i].getDestino():
                return True
        return False         
          
    def obtenerVertice(self, origen):
        for i in range(len(self.list_vertices)):
            if origen == self.list_vertices[i].getData():
                return self.list_vertices[i]
    
    '''METODOS QUE MUESTRAN LA LISTA DE VERTICES'''
    def showVertices(self):
        self.__showVertices(self.list_vertices)
    
    def __showVertices(self, list):
        for i in range(len(list)):
            print(list[i].getData())
    
    '''METODOS PARA MOSTRAR ARISTAS'''
    def showAristas(self):
        self.__showAristas(self.list_aristas)
    
    def __showAristas(self, list):
        for i in range(len(list)):
            print(f"Origen: {list[i].getOrigen()}. Destino: {list[i].getDestino()}. Peso: {list[i].getPeso()}")

    '''METODO QUE MUESTRA LA LISTA DE ADYACENCIA DE TODOS LOS VERTICES'''
    def showListsAdy(self):
        for i in range(len(self.list_vertices)):
            print(f"{self.list_vertices[i].getData()}: {self.list_vertices[i].getListAdy()}")
            
    '''HACE EL RECORRIDO POR LOS VERTICES EN BASE A LA MATRIZ DE ADYACENCIA DEL VERTICE Y SE CREA UNA LISTA CON LOS VERTICES VISITADOS'''
    def recorridoEnProfundidad(self, dato):
        return self.showVisitados(self.__recorridoEnProfundidad(dato, []))
    
    def __recorridoEnProfundidad(self, dato, list):
        if dato in list:
            return
        else:
            vertice = self.obtenerVertice(dato)
            if vertice != None:
                list.append(vertice.getData())
                for dato in vertice.getListAdy():
                    self.__recorridoEnProfundidad(dato, list)
        return list
            
    '''RECORRIDO EN AMPLITUD'''
    def recorridoEnAmplitud(self, dato):
        return self.showVisitados(self.__recorridoEnAmplitud(dato, []))
    
    def __recorridoEnAmplitud(self, dato, list):
        cola = deque()
        vertice = self.obtenerVertice(dato)
        if vertice != None:
            list.append(dato)
            cola.append(vertice)
        while cola:
            elemento = cola.popleft()
            for adyacencia in elemento.getListAdy():
                if adyacencia not in list:
                    vertice = self.obtenerVertice(adyacencia)
                    list.append(adyacencia)
                    cola.append(vertice)
        return list
    
    '''MUESTRA LOS VERTICES VISITADOS '''
    def showVisitados(self, list):
        # my_list = sorted(list) # sorted() ordena alfabeticamente los elementos de la lista
        print(f"los vertices visitados han sido {len(list)}")
        for i in list:
            print(i)

    '''METODO QUE MUESTRA LA LISTA DE ADYACENCIA DE CUALQUIER VERTICE'''
    def showListAdyVertice(self, dato):
        for i in range(len(self.list_vertices)):
            if dato == self.list_vertices[i].getData():
                print(self.list_vertices[i].getListAdy())
    
    '''METODOS PARA IDENTIFICAR LOS NODOS POZO'''
    def verticesPozo(self):
        return print(f"Vértices pozo: {self.__verticesPozo(self.list_vertices)}")
    
    def __verticesPozo(self, list):
        pozos = []
        for vertice in list:
            if len(vertice.getListAdy()) == 0:
                pozos.append(vertice.getData())
        return pozos
    
    '''METODO PARA IDENTIFICAR SI UN NODO ES FUENTE'''
    def esFuente(self, vertice):
        for i in self.list_vertices:
            for j in i.getListAdy():
                if j == vertice:
                    return False
        return True
    
    '''METODOS PARA IDENTIFICAR LOS NODOS FUENTE'''
    def verticesFuente(self):
        return print(f"Vértices fuente: {self.__verticesFuente([])}")
    
    def __verticesFuente(self, fuentes):
        for vertice in self.list_vertices:
            if self.esFuente(vertice.getData()):
                fuentes.append(vertice.getData())
        return fuentes

    '''Grado de los vertices'''
    def gradoVerticesSalida(self):
        cont = 0
        salida = []
        for v in range(len(self.list_vertices)):
            cont = len(self.list_vertices[v].getListAdy())
            salida.append(cont)
        return salida

    def gradoVerticesEntrada(self):
        entrada = []
        for v in range(len(self.list_vertices)):
            dato = self.list_vertices[v].getData()
            cont = 0
            for a in self.list_vertices[v].getListAdy():
                if dato == a:
                    cont += 1
            entrada.append(cont)
        return entrada

    """ALGORITMO KRUSKAL"""
    """Recorrido de Grafo"""

    def quick_sort(self, array):
        lenght = len(array)
        if lenght <= 1:
            return array
        else:
            pivot = array.pop()

        items_greater = []
        items_lower = []

        for item in array:
            if item.getPeso() > pivot.getPeso():
                items_greater.append(item)
            else:
                items_lower.append(item)
        return self.quick_sort(items_lower) + [pivot] + self.quick_sort(items_greater)

    def kruskal(self):
        copiaAristas = self.quick_sort(
            self.ListaAristas
        )  # Copia de la lista de aristas originales ordenada
        aristasKruskal = []
        listaConjuntos = []
        # self.quick_sort(copiaAristas)#Ordenamiento de la copia de aristas
        for menor in copiaAristas:
            self.operacionesConjuntos(menor, listaConjuntos, aristasKruskal)
        # Esta ordenada de menor a mayor
        lista = []
        # print("la lista de conjunto se redujo a : {0}".format(len(ListaConjuntos)))
        for dato in aristasKruskal:
            lista.append([dato.getOrigen(), dato.getDestino()])
        print(lista)
        return lista