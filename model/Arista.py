class Arista:
    '''DEFINE EL NODO ORIGEN Y DESTINO CON SU PESO'''
    def __init__(self, origen, destino, peso):
        self.__origen = origen #nodo o vertice origen
        self.__destino = destino #nodo o vertice destino
        self.__peso = peso #peso o longitud de la arista
        
    def getOrigen(self):
        return self.__origen
    
    def getDestino(self):
        return self.__destino
    
    def getPeso(self):
        return self.__peso
    
    def setOrigen(self, newOrigen):
        self.__origen = newOrigen
        
    def setDestino(self, newDestino):
        self.__destino = newDestino
        
    def setPeso(self, newPeso):
        self.__peso = newPeso