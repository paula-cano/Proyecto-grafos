from model.Vertice import Vertice
from model.Arista import Arista
from collections import deque
from model.LoadFiles import Files


class Grafo:
    
    def createGrafo(self):
        datos = Files.load_data()
        if datos is not None:
            self.createPlanets(datos, 0)
            self.createPaths(datos, 0)
    
    def createPlanets(self, datos, i):
        if i == len(datos["planetas"]):
            return
        self.ingresarVertices(datos["planetas"][i]["nombre"])
        self.createPlanets(datos, i + 1)
    
    def createPaths(self, datos, i):
        if i == len(datos["caminos"]):
            return
        self.ingresarArista(datos["caminos"][i]["origen"], datos["caminos"][i]["destino"], datos["caminos"][i]["peso"])
        self.createPaths(datos, i + 1)
        
    '''DEFINE AL GRAFO CON UNA LISTA VACÍA DE VERTICES Y ARISTAS'''
    def __init__(self):
        self.list_vertices = []
        self.list_aristas = []
        self.createGrafo()
        
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
                self.list_aristas.append(Arista(destino, origen, peso))
                self.obtenerVertice(origen).getListAdy().append(destino)
                self.obtenerVertice(destino).getListAdy().append(origen)
          
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
            for u in range(len(self.list_vertices)):
                if u != v:  # No comparar con el mismo vértice
                    if dato in self.list_vertices[u].getListAdy():
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
            self.list_aristas
        )  # Copia de la lista de aristas originales ordenada
        aristasKruskal = []
        listaConjuntos = []
        # self.quick_sort(copiaAristas)#Ordenamiento de la copia de aristas
        for menor in copiaAristas:
            self.operacionesConj(menor, listaConjuntos, aristasKruskal)
        # Esta ordenada de menor a mayor
        lista = []
        # print("la lista de conjunto se redujo a : {0}".format(len(ListaConjuntos)))
        for dato in aristasKruskal:
            lista.append([dato.getOrigen(), dato.getDestino()])
        print(lista)
        return lista
    
    def operacionesConj(self, menor, listaConjuntos, aristasKruskal):
        encontrados1 = -1
        encontrados2 = -1

        if not listaConjuntos:  # Si esta vacia la lista
            listaConjuntos.append({menor.getOrigen(), menor.getDestino()})
            aristasKruskal.append(menor)
        else:
            for i in range(len(listaConjuntos)):
                if (menor.getOrigen() in listaConjuntos[i]) and (
                        menor.getDestino() in listaConjuntos[i]
                ):
                    return False  ##Camino ciclico

            for i in range(len(listaConjuntos)):
                if menor.getOrigen() in listaConjuntos[i]:
                    encontrados1 = i
                if menor.getDestino() in listaConjuntos[i]:
                    encontrados2 = i

            if encontrados1 != -1 and encontrados2 != -1:
                if (
                        encontrados1 != encontrados2
                ):  # Si pertenecen a dos conjuntos diferentes
                    # debo unir los dos conjuntos
                    # print(encontrados1," ",encontrados2)
                    listaConjuntos[encontrados1].update(
                        listaConjuntos[encontrados2]
                    )  # Uno los dos conjuntos
                    listaConjuntos[encontrados2].clear()  # Elimino el conjunto
                    aristasKruskal.append(menor)

            if (
                    encontrados1 != -1 and encontrados2 == -1
            ):  # Si el origen esta unido a un conjunto
                # listaConjuntos[encontrados1].add(menor.getOrigen())
                listaConjuntos[encontrados1].add(menor.getDestino())
                aristasKruskal.append(menor)

            if (
                    encontrados1 == -1 and encontrados2 != -1
            ):  # Si el destino esta unido a un conjunto
                listaConjuntos[encontrados2].add(menor.getOrigen())
                # listaConjuntos[encontrados2].add(menor.getDestino())
                aristasKruskal.append(menor)

            if encontrados1 == -1 and encontrados2 == -1:
                listaConjuntos.append({menor.getOrigen(), menor.getDestino()})
                aristasKruskal.append(menor)
    
    '''KRUSKAL'''
    def Kruskal(self):
        copy_aristas = self.list_aristas.copy()
        aristas_kruskal = []
        list_conjuntos = []
        
        self.ordenarAristas(copy_aristas)
        for aristaMenor in copy_aristas:
            self.operacionesConjuntos(aristaMenor, list_conjuntos, aristas_kruskal)
            
        for dato in aristas_kruskal:
            print(f"Origen: {dato.getOrigen()}. Destino: {dato.getDestino()}. Peso: {dato.getPeso()}")
    
    def operacionesConjuntos(self, aristaMenor, list_conjuntos, aristas_kruskal):
        found_one = -1
        found_two = -1
        
        if not list_conjuntos:
            list_conjuntos.append({aristaMenor.getOrigen(), aristaMenor.getDestino()})
            aristas_kruskal.append(aristaMenor)
        else:
            for i in range(len(list_conjuntos)):
                if (aristaMenor.getOrigen() in list_conjuntos[i]) and (aristaMenor.getDestino() in list_conjuntos[i]):
                    return False
                
            for i in range(len(list_conjuntos)):
                if aristaMenor.getOrigen() in list_conjuntos[i]:
                    found_one = i
                if aristaMenor.getDestino() in list_conjuntos[i]:
                    found_two = i
                    
            if found_one != -1 and found_two != -1:
                if found_one != found_two:
                    list_conjuntos[found_one].update(list_conjuntos[found_two])
                    list_conjuntos[found_two].clear()
                    aristas_kruskal.append(aristaMenor)
            
            if found_one != -1 and found_two == -1:
                list_conjuntos[found_one].add(aristaMenor.getOrigen())
                list_conjuntos[found_one].add(aristaMenor.getDestino())
                aristas_kruskal.append(aristaMenor)
                
            if found_one == -1 and found_two != -1:
                list_conjuntos[found_two].add(aristaMenor.getOrigen())
                list_conjuntos[found_two].add(aristaMenor.getDestino())
                aristas_kruskal.append(aristaMenor)
                
            if found_one == -1 and found_two == -1:
                list_conjuntos.append({aristaMenor.getOrigen(), aristaMenor.getDestino()})
                aristas_kruskal.append(aristaMenor)
                
    
    def ordenarAristas(self, aristas):
        for i in range(len(aristas)):
            for j in range(i, len(aristas)):
                if aristas[i].getPeso() > aristas[j].getPeso():
                    t = aristas[i]
                    aristas[i] = aristas[j]
                    aristas[j] = t