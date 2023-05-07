class Vertice:
    '''DEFINE EL NOMBRE DEL VERTICE Y SU LISTA DE ADYACENCIAS'''
    def __init__(self, data):
        self.__data = data
        self.list_adyacencia = []
        
    def getData(self):
        return self.__data
    
    def setData(self, newData):
        self.__data = newData
        
    def getListAdy(self):
        return self.list_adyacencia
    