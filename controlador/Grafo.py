from modelo.Vertice import Vertice
from modelo.Arista import Arista

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
    
    '''METODOS QUE MUESTRAN LA LISTA DE VERTICES'''
    def showVertices(self):
        self.__showVertices(self.list_vertices)
    
    def __showVertices(self, list):
        for i in range(len(list)):
            print(list[i].getData())
    
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
    
    '''METODO QUE MUESTRA LA LISTA DE ADYACENCIA DE CUALQUIER VERTICE'''
    def showListAdyVertice(self, dato):
        for i in range(len(self.list_vertices)):
            if dato == self.list_vertices[i].getData():
                print(self.list_vertices[i].getListAdy())
    
    '''METODO QUE MUESTRA LA LISTA DE ADYACENCIA DE TODOS LOS VERTICES'''
    def showListsAdy(self):
        for i in range(len(self.list_vertices)):
            print(f"{self.list_vertices[i].getData()}: {self.list_vertices[i].getListAdy()}")
            
    '''METODOS PARA MOSTRAR ARISTAS'''
    def showAristas(self):
        self.__showAristas(self.list_aristas)
    
    def __showAristas(self, list):
        for i in range(len(list)):
            print(f"Origen: {list[i].getOrigen()}. Destino: {list[i].getDestino()}. Peso: {list[i].getPeso()}")